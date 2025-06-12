-- Query: Top 5 highest-rated products
SELECT TOP 5 
    title,
    rating,
    price,
    category
FROM products
ORDER BY rating DESC;
