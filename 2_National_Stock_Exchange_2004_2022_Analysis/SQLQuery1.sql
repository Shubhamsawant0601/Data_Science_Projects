-- ==============================================================================================================================
-- 5 Days Rolling Average for the Average Closing price of the stocks
-- ==============================================================================================================================

SELECT  Symbol, 
		"Close", 
		"Date",
		AVG("Close") OVER (PARTITION BY Symbol ORDER BY "Date" ASC ROWS BETWEEN 5 PRECEDING AND CURRENT ROW) AS Average_Close
FROM [dbo].[national_stock_exchange_2004_2022_cleaned]
-- ==============================================================================================================================
