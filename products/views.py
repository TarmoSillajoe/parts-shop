from django import shortcuts
from .models import Merchant
from django import db
from django import http
from .forms import CrossRefForm


def home(request):
    return shortcuts.render(request, template_name="home.html", context={})


def merchants(request):
    merchants = Merchant.objects.all()
    return shortcuts.render(
        request, template_name="merchants.html", context={"merchants": merchants}
    )


def code_query_form(request):
    form = CrossRefForm(request.GET)
    if form.is_valid():
        code = form.cleaned_data["code"]
        return shortcuts.redirect(shortcuts.reverse("cross_refs") + f"?code={code}")
    return shortcuts.render(request, "crossref_form.html", {"form": form})


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def cross_refs(request):
    code = request.GET["code"]
    with db.connection.cursor() as cursor:
        cursor.execute(
            """
with q(code) as (
    values (%s)
),
bao as (
    select item_id,
        code as bao
    from merchant_item
    where merchant_id = 1
    union
    select item_id, code as bao
    from merchant_item
    where merchant_id = 2
)
select bao, bitem.code,
    manufacturer.name as brand,
    mi.code as merchants_code,
    round(mi.purchase_price, 2) as price,
    mi.min_order,
    merchant.name as merchant,
    mi.modified_at
from q
    join item using(code)
    join item bitem using(base_item_id)
    join manufacturer on bitem.manufacturer_id = manufacturer.id
    join merchant_item mi on bitem.id = mi.item_id
    join merchant on mi.merchant_id = merchant.id
    left join bao using(item_id)
where modified_at > '2023-06-01' and mi.merchant_id not in (1)
order by brand limit 30;
                       """,
            [code],
        )
        results = dict_fetchall(cursor)
    return shortcuts.render(
        request,
        template_name="crossrefs.html",
        context={"results": results, "code": code},
    )


def applesauce(request):
    results = []
    form = CrossRefForm()
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
                        code as bao
                    from merchant_item
                    where merchant_id = 1
                    union
                    select item_id, code as bao
                    from merchant_item
                    where merchant_id = 2
                )
                select bao, bitem.code,
                    manufacturer.name as brand,
                    mi.code as merchants_code,
                    round(mi.purchase_price, 2) as price,
                    mi.min_order,
                    merchant.name as merchant,
                    mi.modified_at
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
    return shortcuts.render(request, "applesauce.html", context)
