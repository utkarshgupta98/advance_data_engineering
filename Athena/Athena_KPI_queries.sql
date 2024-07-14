-- Inventory Turnover Ratio measures how efficiently inventory is managed by indicating how many times inventory is sold and replaced over a period.

SELECT 
    SUM(InvoiceTotal) / SUM(Quantity) AS InventoryTurnoverRatio
FROM 
    transformed_data
WHERE 
    Year = 2011;


-- Stockout Rate measures the percentage of time products are out of stock.

SELECT 
    COUNT(DISTINCT InvoiceNo) AS StockoutCount
FROM 
    transformed_data
WHERE 
    Quantity = 0
    AND Year = 2011;


-- COGS to Revenue Ratio measures the efficiency of managing inventory costs relative to revenue.

SELECT 
    SUM(Quantity * UnitPrice) / SUM(InvoiceTotal) AS COGSToRevenueRatio
FROM 
    transformed_data
WHERE 
    Year = 2011;


-- Customer Acquisition Cost (CAC) measures the average cost of acquiring a new customer.

SELECT 
    SUM(InvoiceTotal) / COUNT(DISTINCT CustomerID) AS CAC
FROM 
    transformed_data
WHERE 
    Year = 2011;


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


-- Average Order Value (AOV): Measures the average amount spent per order over the course of the year 2011.

SELECT 
    AVG(InvoiceTotal) AS AOV
FROM 
    transformed_data
WHERE 
    Year = 2011;
	

-- Gross Margin: Measures the profitability of products by comparing the revenue (InvoiceTotal) to the cost of goods sold (Quantity * UnitPrice).	
	
SELECT 
    SUM(InvoiceTotal - (Quantity * UnitPrice)) / SUM(InvoiceTotal) AS GrossMargin
FROM 
    transformed_data
WHERE 
    Year = 2011;

