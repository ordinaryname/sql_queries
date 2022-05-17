-- https://www.sql-practice.com/
SELECT * FROM patients LIMIT 1;
-- Show patient id, first name, last name, gender, height where patient is above average patient height
SELECT patient_id, first_name, last_name, gender, height FROM patients WHERE height > (SELECT AVG(height) FROM patients) LIMIT 10;
-- Show first name and last name of patients without allergies
SELECT first_name, last_name FROM patients WHERE allergies IS NULL;
-- Show first name, last name, and admissions date
SELECT admissions.patient_id, patients.first_name, admissions.admission_date
FROM admissions
LEFT JOIN patients
ON patients.patient_id = admissions.patient_id
LIMIT 10
-- Join first name and last name into full name column
SELECT first_name || ' ' || last_name AS full_name
FROM patients
-- Show first name, last name, and full province name
SELECT patients.first_name, patients.last_name, provinces.province_name
FROM patients
LEFT JOIN provinces ON provinces.province_id = patients.province_id
-- Count how many patients were born in 2010
WITH births
AS (
  SELECT YEAR(birth_date) AS birth_year
  FROM patients
  WHERE birth_year = 2010
  )
SELECT COUNT(birth_year)
FROM births
