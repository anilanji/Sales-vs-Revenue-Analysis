# KPI Queries
total_sales = "SELECT SUM(sales) FROM superstore"

avg_order_value = """
SELECT ROUND(SUM(sales)/COUNT(DISTINCT order_id),2) 
AS avg_order_value
FROM superstore
"""

# Customer Analysis
top_customers = """
SELECT customer_name,
ROUND(SUM(sales),2) AS total_spent
FROM superstore
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 10
"""

# Region Analysis
region_performance = """
SELECT region,
ROUND(SUM(sales),2) AS total_sales,
ROUND(SUM(profit),2) AS total_profit
FROM superstore
GROUP BY region
"""

# Time Analysis
yearly_sales = """
SELECT year,
ROUND(SUM(sales),2) AS total_sales
FROM superstore
GROUP BY year
ORDER BY year
"""

monthly_sales = """
SELECT month,
ROUND(SUM(sales),2) AS total_sales
FROM superstore
GROUP BY month
ORDER BY month
"""

category_sales ="""
select category,round (sum(profit),2)as total_profit,
round(sum(sales),2) as total_sales from superstore group by category"""

category_yearly_performance = """
SELECT 
    year,
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM superstore
GROUP BY year, category
ORDER BY year, category;
"""


names_customers = """
SELECT 
    customer_name,
    category, 
    ROUND(SUM(sales), 2) AS total_spent 
FROM superstore
GROUP BY customer_name, category
ORDER BY total_spent DESC, category
LIMIT 5;
"""
