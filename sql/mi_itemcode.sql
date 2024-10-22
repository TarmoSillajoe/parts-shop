with invoice(code, qty, price) as(
    values ('4329015002', 5, 40.00),
        ('4329012512', 5, 25.00),
        ('4329012232', 50, 25.00),
        ('9253761000', 1, 100.00)
),
seller_item as (
    select min(min_order),
        item_id,
        code
    from merchant_item mi
    where mi.merchant_id = 5
    group by item_id,
        code
),
bao_item as (
    select item_id,
        code as bao,
        description as bao_descr
    from merchant_item bao
    where bao.merchant_id = 1
),
koivunen_item as (
    select item_id,
        code as koivunen,
        description as koivunen_descr
    from merchant_item
    where merchant_item.merchant_id = 2
)
select coalesce(bao, koivunen) as bao,
    invoice.qty,
    invoice.price,
    invoice.code,
    coalesce(bao_descr, koivunen_descr) as description
from invoice
    left join seller_item using(code)
    left join bao_item using(item_id)
    left join koivunen_item using(item_id);