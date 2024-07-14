-- COGS to Revenue Ratio measures the efficiency of managing inventory costs relative to revenue.

SELECT 
    SUM(Quantity * UnitPrice) / SUM(InvoiceTotal) AS COGSToRevenueRatio
FROM 
    transformed_data
WHERE 
    Year = 2011;