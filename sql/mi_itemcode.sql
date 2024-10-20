select count(*) as n,
    merchant.name
from merchant_item mi
    join merchant on mi.merchant_id = merchant.id
group by merchant.name
order by n desc;
-----------
-----------
select count(*) as n,
    manufacturer.name
from item
    join manufacturer on item.manufacturer_id = manufacturer.id
group by manufacturer.name
order by n desc;
---------------
select code,ean,
    purchase_price,
    description,
    to_char(modified_at, 'YYYY-mm')
from merchant_item
join ean using(item_id)
where merchant_id = 32
order by merchant_item.id asc
limit 15 offset 20;