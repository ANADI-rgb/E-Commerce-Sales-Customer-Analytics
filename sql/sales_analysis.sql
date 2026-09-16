USE ecommerce_analytics;

-- =====================================================
-- E-COMMERCE SALES & CUSTOMER ANALYTICS
-- SQL ANALYSIS
-- =====================================================


-- =====================================================
-- 1. OVERALL BUSINESS KPIs
-- =====================================================

SELECT
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    COUNT(DISTINCT product_id) AS total_products,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(cost), 2) AS total_cost,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(AVG(profit_margin), 2) AS avg_profit_margin
FROM orders;


-- =====================================================
-- 2. AVERAGE ORDER VALUE
-- =====================================================

SELECT
    ROUND(SUM(revenue) / COUNT(DISTINCT order_id), 2)
        AS average_order_value
FROM orders;


-- =====================================================
-- 3. MONTHLY SALES PERFORMANCE
-- =====================================================

SELECT
    order_year,
    order_month,
    month_name,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders
FROM orders
GROUP BY
    order_year,
    order_month,
    month_name
ORDER BY
    order_year,
    order_month;


-- =====================================================
-- 4. CATEGORY PERFORMANCE
-- =====================================================

SELECT
    category,
    SUM(quantity) AS units_sold,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(cost), 2) AS total_cost,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(
        SUM(profit) / NULLIF(SUM(revenue), 0) * 100,
        2
    ) AS profit_margin
FROM orders
GROUP BY category
ORDER BY total_revenue DESC;


-- =====================================================
-- 5. REGIONAL PERFORMANCE
-- =====================================================

SELECT
    region,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(
        SUM(profit) / NULLIF(SUM(revenue), 0) * 100,
        2
    ) AS profit_margin
FROM orders
GROUP BY region
ORDER BY total_revenue DESC;


-- =====================================================
-- 6. TOP 10 PRODUCTS BY REVENUE
-- =====================================================

SELECT
    product_id,
    product_name,
    category,
    SUM(quantity) AS units_sold,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit
FROM orders
GROUP BY
    product_id,
    product_name,
    category
ORDER BY total_revenue DESC
LIMIT 10;


-- =====================================================
-- 7. TOP 10 PRODUCTS BY PROFIT
-- =====================================================

SELECT
    product_id,
    product_name,
    category,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM orders
GROUP BY
    product_id,
    product_name,
    category
ORDER BY total_profit DESC
LIMIT 10;


-- =====================================================
-- 8. TOP 10 CUSTOMERS BY REVENUE
-- =====================================================

SELECT
    customer_id,
    customer_name,
    region,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit
FROM orders
GROUP BY
    customer_id,
    customer_name,
    region
ORDER BY total_revenue DESC
LIMIT 10;


-- =====================================================
-- 9. RETURN ANALYSIS
-- =====================================================

SELECT
    returned,
    COUNT(*) AS total_orders,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders),
        2
    ) AS return_percentage,
    ROUND(SUM(revenue), 2) AS revenue
FROM orders
GROUP BY returned
ORDER BY total_orders DESC;


-- =====================================================
-- 10. RETURN RATE BY CATEGORY
-- =====================================================

SELECT
    category,
    COUNT(*) AS total_orders,
    SUM(return_flag) AS returned_orders,
    ROUND(
        SUM(return_flag) * 100.0 / COUNT(*),
        2
    ) AS return_rate
FROM orders
GROUP BY category
ORDER BY return_rate DESC;


-- =====================================================
-- 11. PROFITABLE VS LOSS-MAKING ORDERS
-- =====================================================

SELECT
    CASE
        WHEN profit > 0 THEN 'Profitable'
        WHEN profit < 0 THEN 'Loss Making'
        ELSE 'Break Even'
    END AS order_status,
    COUNT(*) AS order_count,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit
FROM orders
GROUP BY order_status;


-- =====================================================
-- 12. DISCOUNT VS PROFIT ANALYSIS
-- =====================================================

SELECT
    CASE
        WHEN discount = 0 THEN 'No Discount'
        WHEN discount <= 0.10 THEN 'Low Discount'
        WHEN discount <= 0.20 THEN 'Medium Discount'
        ELSE 'High Discount'
    END AS discount_category,
    COUNT(*) AS total_orders,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(SUM(profit), 2) AS profit,
    ROUND(AVG(profit_margin), 2) AS avg_profit_margin
FROM orders
GROUP BY discount_category
ORDER BY avg_profit_margin DESC;


-- =====================================================
-- 13. CITY PERFORMANCE
-- =====================================================

SELECT
    city,
    region,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit
FROM orders
GROUP BY
    city,
    region
ORDER BY total_revenue DESC
LIMIT 20;


-- =====================================================
-- 14. QUARTERLY PERFORMANCE
-- =====================================================

SELECT
    order_year,
    order_quarter,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders
FROM orders
GROUP BY
    order_year,
    order_quarter
ORDER BY
    order_year,
    order_quarter;