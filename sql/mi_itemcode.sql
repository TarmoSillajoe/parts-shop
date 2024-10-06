select mi.code,
    mi.description,
    item.code as itemcode,
    item.base_item_id
from merchant_item mi
    join item on mi.item_id = item.id
where mi.merchant_id in ((select id from merchant where name ilike '%k%s%tools%'))
order by mi.id desc
limit 50;