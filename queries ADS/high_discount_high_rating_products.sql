--------------------------------------------------------
-- Query 2: High-Discount Products with Excellent Rating
-- Purpose: Identify products that have significant discounts 
--           (>10%), excellent ratings, and high stock levels.
--           Calculates the total potential savings (€) 
--           from available inventory.
--------------------------------------------------------

SELECT 
    title AS [Product Title],                        -- Product name
    category AS [Category],                          -- Product category
    CAST(discountPercentage AS DECIMAL(5,2)) AS [Discount %],  -- Discount percentage
    CAST(rating AS DECIMAL(4,2)) AS [Rating],        -- Rounded product rating
    stock AS [Stock Units],                          -- Units available in stock
    CONCAT(ROUND((price - finalPrice) * stock, 2), ' €') AS [Total Savings (€)]  
                                                     -- Total potential savings in euros
FROM dbo.Products_Enriched
WHERE 
    discountPercentage > 10                          -- Only products with more than 10% discount
    AND ratingCategory = 'Excellent'                 -- Products rated as "Excellent"
    AND stockAlertLevel = 'High Stock'               -- Products with high stock level
ORDER BY 
    (price - finalPrice) * stock DESC;               -- Sort by total savings (descending)




