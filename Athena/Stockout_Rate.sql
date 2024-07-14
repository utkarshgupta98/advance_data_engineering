-- Stockout Rate measures the percentage of time products are out of stock.

SELECT 
    COUNT(DISTINCT InvoiceNo) AS StockoutCount
FROM 
    transformed_data
WHERE 
    Quantity = 0
    AND Year = 2011;