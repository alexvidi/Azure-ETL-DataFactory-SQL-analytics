--------------------------------------------------------
-- Query 1: Average Rating and Product Count by Category
-- Purpose: Calculates the average rating and total number 
--          of products per category, showing which segments 
--          perform best in customer satisfaction.
--------------------------------------------------------

SELECT 
    category,
    CAST(AVG(rating) AS DECIMAL(5,2)) AS AverageRating,  -- Rounded average rating
    COUNT(*) AS TotalProducts                             -- Total number of products in each category
FROM dbo.Products_Enriched
GROUP BY category
ORDER BY AverageRating DESC;  -- Highest-rated categories appear first



