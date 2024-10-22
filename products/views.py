from django import shortcuts
from .models import Merchant, Item
from django import db
from django import http
from .forms import CrossRefForm, MerchantSearchForm, UploadInvoiceForm
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.http import HttpResponse
import csv


def dict_fetchall(cursor) -> list[dict]:
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def processed_invoice(request):
    return HttpResponse("<h1>Processed your stuff</h1>")


def process_csv(uploaded_file, merchant_id: int):
    invoice_data: list = []
    decoded_file = uploaded_file.read().decode("utf-8")
    csv_reader = csv.DictReader(
        decoded_file.splitlines(),
        fieldnames=["code", "qty", "price"],
        quotechar='"',
    )
    for row in csv_reader:
        invoice_data.append(row)
    invoice_values = ", ".join(
        f"('{row['code']}',{row['qty']},{row['price']})" for row in invoice_data
    )

    query = f"""
    WITH invoice(code, qty, price) AS (
        VALUES {invoice_values}
    ),
    seller_item AS (
        SELECT MIN(min_order),
            item_id,
            code
        FROM merchant_item mi
        WHERE mi.merchant_id = %s
        GROUP BY item_id, code
    ),
    bao_item AS (
        SELECT item_id,
            code AS bao,
            description AS bao_descr
        FROM merchant_item bao
        WHERE bao.merchant_id = 1
    ),
    koivunen_item AS (
        SELECT item_id,
            code AS koivunen,
            description AS koivunen_descr
        FROM merchant_item
        WHERE merchant_item.merchant_id = 2
    )
    SELECT COALESCE(bao, koivunen) AS bao,
        invoice.qty,
        invoice.price,
        invoice.code,
        COALESCE(bao_descr, koivunen_descr) AS description
    FROM invoice
    LEFT JOIN seller_item USING(code)
    LEFT JOIN bao_item USING(item_id)
    LEFT JOIN koivunen_item USING(item_id);
    """
    with db.connection.cursor() as cursor:
        cursor.execute(query, [merchant_id])
        results = dict_fetchall(cursor)
    return results


def upload_invoice(request, merchantid: int):
    if request.method == "POST":
        uploadform: UploadInvoiceForm = UploadInvoiceForm(request.POST, request.FILES)
        if uploadform.is_valid():
            processing_results = process_csv(
                request.FILES["file"], merchant_id=merchantid
            )
            return shortcuts.render(
                request,
                "upload_invoice.html",
                context={
                    "processing_results": processing_results,
                    "uploadform": uploadform,
                    "merchantid": merchantid,
                },
            )
    else:
        uploadform = UploadInvoiceForm()
        context = {"uploadform": uploadform, "merchantid": merchantid}
    return shortcuts.render(
        request, template_name="upload_invoice.html", context=context
    )


def invoice(request):
    merchant_id: int = request.GET.get("merchantid")
    merchant_name: str = request.GET.get("name")

    merchant_form = MerchantSearchForm(initial={"name": merchant_name})
    context = {"merchant_form": merchant_form, "merchant_id": merchant_id}

    return shortcuts.render(
        request,
        template_name="invoice.html",
        context=context,
    )


def merchant_search(request):
    name_fragment: str = request.GET.get("name")
    if name_fragment:
        result = Merchant.objects.filter(name__istartswith=name_fragment).values()
        return shortcuts.render(
            request,
            template_name="merchants_found.html",
            context={"merchants_found": result},
        )


def code_search(request):
    code_fragment: str = request.GET.get("code")
    if code_fragment and len(code_fragment) > 2:
        result = Item.objects.filter(
            base_item__isnull=False,
            code__istartswith=code_fragment,
        ).values()
        return shortcuts.render(
            request,
            template_name="codes_found.html",
            context={"items_found": result},
        )


def applesauce(request):
    results = []
    form: CrossRefForm = CrossRefForm()
    context = {"form": form}
    if "code" in request.GET:
        form = CrossRefForm(request.GET)
        if form.is_valid():
            code: str = form.cleaned_data["code"]
            with db.connection.cursor() as cursor:
                cursor.execute(
                    """
                with q(code) as (
                    values (%s)
                ),
                bao as (
                    select item_id,
                        code as bao, description
                    from merchant_item
                    where merchant_id = 1
                    union
                    select item_id, code as bao, description
                    from merchant_item
                    where merchant_id = 2
                )
                select bao, bitem.code,
                    manufacturer.name as brand,
                    mi.code as merchants_code,
                    round(mi.purchase_price, 2) as price,
                    mi.min_order,
                    merchant.name as merchant,
                    mi.modified_at, bao.description
                from q
                    join item using(code)
                    join item bitem using(base_item_id)
                    join manufacturer on bitem.manufacturer_id = manufacturer.id
                    join merchant_item mi on bitem.id = mi.item_id
                    join merchant on mi.merchant_id = merchant.id
                    left join bao using(item_id)
                where modified_at > '2023-06-01' and mi.merchant_id not in (1)
                order by brand, bao;
                       """,
                    [code],
                )
                results = dict_fetchall(cursor)
                if results:
                    context.update({"results": results})
            context.update({"form": CrossRefForm(form.cleaned_data)})
    return shortcuts.render(request, "applesauce.html", context)
