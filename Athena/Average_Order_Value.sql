-- Average Order Value (AOV): Measures the average amount spent per order over the course of the year 2011.

SELECT 
    AVG(InvoiceTotal) AS AOV
FROM 
    transformed_data
WHERE 
    Year = 2011;