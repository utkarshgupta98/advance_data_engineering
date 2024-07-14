-- Returning Customers: The total number of unique customers who made purchases on July 11, 2011.

SELECT 
    COUNT(DISTINCT CustomerID) AS ReturningCustomers,
    COUNT(DISTINCT CASE WHEN Quantity > 0 THEN CustomerID ELSE NULL END) AS TotalCustomers
FROM 
    transformed_data
WHERE 
    Year = 2011
    AND Month = 7
    AND DayOfMonth = 11;