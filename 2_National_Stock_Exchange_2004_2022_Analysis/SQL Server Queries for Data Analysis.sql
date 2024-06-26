-- ====================================================================================================
-- Get the highest price for the each company and belonging to each industry 

SELECT Industry, 
	   Symbol, 
	   MAX(High) AS Highest_Stock_Price
FROM dbo.national_stock_exchange_2004_2022_cleaned
GROUP BY Symbol, Industry
ORDER BY Highest_Stock_Price DESC;
-- ====================================================================================================

-- Get the lowest price for the each company and belonging to each industry 

SELECT Industry, 
	   Symbol, 
	   MIN(Low) AS Lowest_Stock_Price
FROM dbo.national_stock_exchange_2004_2022_cleaned
GROUP BY Symbol, Industry
ORDER BY Lowest_Stock_Price ASC;

-- ====================================================================================================

-- Get the moving average of the closing stock price for all stocks over the period of 2000 to 2021 and moving average period is 15days

SELECT "Date",
    "Symbol",
    AVG("Close") OVER (PARTITION BY "Symbol" ORDER BY "Date" ASC ROWS BETWEEN 15 PRECEDING AND CURRENT ROW) AS Moving_Average_15_Days
FROM dbo.national_stock_exchange_2004_2022_cleaned
ORDER BY "Symbol", "Date";

-- ====================================================================================================

-- Difference between the "High" and "Low" prices for each day and returns the maximum positive difference found in the dataset.

SELECT * 
FROM (SELECT *, (High - Low) AS Max_Positive_Difference
	  FROM dbo.national_stock_exchange_2004_2022_cleaned ) AS subq
WHERE Max_Positive_Difference>0
ORDER BY Max_Positive_Difference DESC

-- ====================================================================================================
