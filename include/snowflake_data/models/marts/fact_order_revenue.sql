select
    o.order_date,
    o.order_id,
    sum(total_price) as total_price
from
{{ref('stg_orders')}} o
LEFT JOIN {{ref('stg_order_items')}} oi
ON o.ORDER_ID = oi.ORDER_ID
GROUP BY 1,2