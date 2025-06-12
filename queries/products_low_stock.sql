-- Query: Products with low stock (less than 30 units)
SELECT 
    id,
    title,
    stock,
    category
FROM products
WHERE stock < 30
ORDER BY stock ASC;
