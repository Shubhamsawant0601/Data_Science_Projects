-- =================================================================================================================================
-- Select all the records from the dataset
SELECT * FROM dbo.heart_disease_prediction

-- Total we have 270 records
-- =================================================================================================================================

-- =================================================================================================================================
-- Age Distribution of Patients with Different Chest Pain Types

SELECT Chest_pain_type, Age, COUNT(*) AS Count
FROM dbo.heart_disease_prediction_cleaned_data
GROUP BY Chest_pain_type, Age
ORDER BY Chest_pain_type, Age;

-- =================================================================================================================================
-- Average age for each type of chest pain
SELECT Chest_pain_type, 
		AVG(Age) AS Age_Average
FROM heart_disease_prediction_cleaned_data
GROUP BY Chest_pain_type

-- =================================================================================================================================
