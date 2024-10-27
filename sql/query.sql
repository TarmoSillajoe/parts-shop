with q(code) as (
    values (
            'GDB5121'
        )
),
bao as (
    select item_id,
        code as bao
    from merchant_item
    where merchant_id = 1
    union
    select item_id,
        code as bao
    from merchant_item
    where merchant_id = 2
)
select bao,
    bitem.code,
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
where modified_at > '2023-06-01'
    and mi.merchant_id not in (1)
order by brand,
    bao;