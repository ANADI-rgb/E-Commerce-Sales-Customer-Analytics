USE ecommerce_analytics;

-- =====================================================
-- POWER BI SALES ANALYTICS VIEW
-- =====================================================

CREATE OR REPLACE VIEW vw_sales_dashboard AS

SELECT
    order_id,
    order_date,
    order_year,
    order_month,
    month_name,
    order_quarter,

    customer_id,
    customer_name,
    customer_type,

    product_id,
    product_name,
    category,
    sub_category,

    city,
    state,
    region,

    quantity,
    selling_price,
    discount,

    revenue,
    cost,
    profit,
    profit_margin,

    returned,
    return_flag

FROM orders;

-- =====================================================
-- POWER BI CUSTOMER RFM VIEW
-- =====================================================

CREATE OR REPLACE VIEW vw_customer_rfm AS

WITH customer_rfm AS (

    SELECT
        customer_id,
        MAX(customer_name) AS customer_name,

        DATEDIFF(
            (SELECT MAX(order_date) FROM orders),
            MAX(order_date)
        ) AS recency,

        COUNT(DISTINCT order_id) AS frequency,

        ROUND(SUM(revenue), 2) AS monetary

    FROM orders

    GROUP BY customer_id
),

rfm_scores AS (

    SELECT
        customer_id,
        customer_name,
        recency,
        frequency,
        monetary,

        NTILE(5) OVER (
            ORDER BY recency DESC
        ) AS r_score,

        NTILE(5) OVER (
            ORDER BY frequency
        ) AS f_score,

        NTILE(5) OVER (
            ORDER BY monetary
        ) AS m_score

    FROM customer_rfm
)

SELECT
    customer_id,
    customer_name,
    recency,
    frequency,
    monetary,
    r_score,
    f_score,
    m_score,

    CONCAT(r_score, f_score, m_score) AS rfm_score,

    CASE
        WHEN r_score >= 4
             AND f_score >= 4
             AND m_score >= 4
            THEN 'Champions'

        WHEN r_score >= 3
             AND f_score >= 4
            THEN 'Loyal Customers'

        WHEN r_score >= 4
             AND f_score >= 2
            THEN 'Potential Loyalists'

        WHEN r_score >= 4
             AND f_score <= 2
            THEN 'New Customers'

        WHEN r_score <= 2
             AND f_score >= 3
            THEN 'At Risk'

        WHEN r_score <= 2
             AND f_score <= 2
            THEN 'Lost Customers'

        ELSE 'Needs Attention'
    END AS customer_segment

FROM rfm_scores;