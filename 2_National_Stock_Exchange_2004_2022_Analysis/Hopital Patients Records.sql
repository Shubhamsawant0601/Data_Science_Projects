/*-- ==================================================================================================
-- Count of patients for each type of surgery
-- ==================================================================================================
SELECT s.DESCRIPTION, COUNT(p.id) AS Count_of_patients
FROM "procedures" s
JOIN "patients" p
ON p.Id=s.PATIENT
GROUP BY s.DESCRIPTION
ORDER BY Count_of_patients DESC


-- ==================================================================================================
-- Total claims for each type of surgery 
-- ==================================================================================================
*/
SELECT s.DESCRIPTION, COUNT(p.id) AS Count_of_patients
FROM "procedures" s
JOIN "patients" p
ON p.Id=s.PATIENT
GROUP BY s.DESCRIPTION
ORDER BY Count_of_patients DESC


