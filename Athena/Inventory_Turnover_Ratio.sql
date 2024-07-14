-- Inventory Turnover Ratio measures how efficiently inventory is managed by indicating how many times inventory is sold and replaced over a period.

SELECT 
    SUM(InvoiceTotal) / SUM(Quantity) AS InventoryTurnoverRatio
FROM 
    transformed_data
WHERE 
    Year = 2011;