copy (
    select index as code,
        cast(quantity as int) as qty,
        "Price net_1"
    from read_csv('/mnt/c/users/tarmos/koik/order_36622565.csv')
) to '/mnt/c/users/tarmos/koik/autos_order.csv';