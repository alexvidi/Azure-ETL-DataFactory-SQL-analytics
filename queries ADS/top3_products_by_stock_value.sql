--------------------------------------------------------
-- Query 3: Top-3 products by stock value per category
-- Purpose: Rank products within each category by total 
--          stock value and return the top 3 per category.
--          Useful to prioritize high-impact inventory.
--------------------------------------------------------

WITH RankedProducts AS (
    SELECT 
        title   AS [Product Title],                   -- Product name
        category AS [Category],                       -- Product category
        CAST(stockValue AS DECIMAL(10,2)) AS [Stock Value (€)], -- Stock value with 2 decimals
        ROW_NUMBER() OVER (                           -- Ranking within each category
            PARTITION BY category 
            ORDER BY stockValue DESC
        ) AS [Rank]
    FROM dbo.Products_Enriched
)
SELECT
    [Product Title],
    [Category],
    CONCAT([Stock Value (€)], ' €') AS [Stock Value (€)],  -- Pretty print with euro symbol
    [Rank]
FROM RankedProducts
WHERE [Rank] <= 3                                         -- Keep top 3 per category
ORDER BY [Category], [Rank];                              -- Stable and readable order

