-- Query: Average price by product category
SELECT category, ROUND(AVG(price), 2) AS avg_price
FROM products
GROUP BY category
ORDER BY avg_price DESC;
