# SQL Queries
Sample queries to showcase my sql skills

## Inside Airbnb
A website (no affiliation with Airbnb) which collects and distributes data about Airbnb listings and hosts in some major cities around the world.<br/>
I used data from this website to create a database to run my queries. The results of some of my queries were exported, using Python, to csv files. These files were used in Excel and Tableau to produce charts and graphs like the ones seen below. Click on the inside_airbnb.sql file to see the queries with my notes.

```sql
-- Count the number of available/unavailable listings grouped by date
SELECT date, available, COUNT(available) FROM Calendar GROUP BY date, available ORDER BY date
```

[Graph of Airbnb Availabilty by Day of the Week](Airbnb_Availability_by_Day_of_the_Week.png)

## SQL-Practice.com
This is a website that makes allows me to create and run queries on a database in the web browser. Their database contains fictitious data about patients in a hospital. Click on the sql_practice.sql file to see the queries with my notes.

```sql
-- Count how many patients were born in 2010
WITH births
AS (
  SELECT YEAR(birth_date) AS birth_year
  FROM patients
  WHERE birth_year = 2010
  )
SELECT COUNT(birth_year)
FROM births
```

## Data Sources
Inside Airbnb : http://insideairbnb.com/get-the-data <br/>
sql_practice.sql : https://www.sql-practice.com/
