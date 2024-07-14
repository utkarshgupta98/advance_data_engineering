-- Gross Margin: Measures the profitability of products by comparing the revenue (InvoiceTotal) to the cost of goods sold (Quantity * UnitPrice).	
	
SELECT 
    SUM(InvoiceTotal - (Quantity * UnitPrice)) / SUM(InvoiceTotal) AS GrossMargin
FROM 
    transformed_data
WHERE 
    Year = 2011;