USE ecommerce_analytics;

-- =====================================================
-- CUSTOMER ANALYTICS
-- =====================================================


-- 1. CUSTOMER SUMMARY
-- =====================================================

SELECT
    COUNT(DISTINCT customer_id) AS total_customers,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(
        SUM(revenue) / COUNT(DISTINCT customer_id),
        2
    ) AS revenue_per_customer
FROM orders;


-- 2. NEW VS RETURNING ORDERS
-- =====================================================
-- First order of each customer = New Customer
-- Later orders = Returning Customer

WITH customer_orders AS (
    SELECT
        order_id,
        customer_id,
        order_date,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date, order_id
        ) AS order_number
    FROM orders
)

SELECT
    CASE
        WHEN order_number = 1 THEN 'New Customer'
        ELSE 'Returning Customer'
    END AS customer_type,
    COUNT(*) AS total_orders,
    COUNT(DISTINCT customer_id) AS customers
FROM customer_orders
GROUP BY
    CASE
        WHEN order_number = 1 THEN 'New Customer'
        ELSE 'Returning Customer'
    END;


-- 3. CUSTOMER REVENUE
-- =====================================================

SELECT
    customer_id,
    customer_name,
    region,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS total_units,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(
        SUM(revenue) / COUNT(DISTINCT order_id),
        2
    ) AS average_order_value
FROM orders
GROUP BY
    customer_id,
    customer_name,
    region
ORDER BY total_revenue DESC
LIMIT 20;


-- 4. CUSTOMER PURCHASE FREQUENCY
-- =====================================================

SELECT
    customer_id,
    customer_name,
    COUNT(DISTINCT order_id) AS purchase_frequency,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM orders
GROUP BY
    customer_id,
    customer_name
ORDER BY purchase_frequency DESC
LIMIT 20;


-- =====================================================
-- 5. RFM BASE DATA
-- =====================================================

WITH customer_rfm AS (
    SELECT
        customer_id,
        customer_name,

        DATEDIFF(
            (SELECT MAX(order_date) FROM orders),
            MAX(order_date)
        ) AS recency,

        COUNT(DISTINCT order_id) AS frequency,

        ROUND(SUM(revenue), 2) AS monetary

    FROM orders

    GROUP BY
        customer_id,
        customer_name
)

SELECT *
FROM customer_rfm
ORDER BY monetary DESC;


-- =====================================================
-- 6. RFM SCORES
-- =====================================================

WITH customer_rfm AS (
    SELECT
        customer_id,
        customer_name,

        DATEDIFF(
            (SELECT MAX(order_date) FROM orders),
            MAX(order_date)
        ) AS recency,

        COUNT(DISTINCT order_id) AS frequency,

        ROUND(SUM(revenue), 2) AS monetary

    FROM orders

    GROUP BY
        customer_id,
        customer_name
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
    CONCAT(r_score, f_score, m_score) AS rfm_score
FROM rfm_scores
ORDER BY monetary DESC;


-- =====================================================
-- 7. RFM CUSTOMER SEGMENTS
-- =====================================================

WITH customer_rfm AS (
    SELECT
        customer_id,
        customer_name,

        DATEDIFF(
            (SELECT MAX(order_date) FROM orders),
            MAX(order_date)
        ) AS recency,

        COUNT(DISTINCT order_id) AS frequency,

        ROUND(SUM(revenue), 2) AS monetary

    FROM orders

    GROUP BY
        customer_id,
        customer_name
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

FROM rfm_scores
ORDER BY monetary DESC;