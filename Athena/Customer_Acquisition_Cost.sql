-- Customer Acquisition Cost (CAC) measures the average cost of acquiring a new customer.

SELECT 
    SUM(InvoiceTotal) / COUNT(DISTINCT CustomerID) AS CAC
FROM 
    transformed_data
WHERE 
    Year = 2011;
