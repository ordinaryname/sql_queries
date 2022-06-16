-- http://insideairbnb.com/get-the-data
-- listing_id,date,available,price,adjusted_price,minimum_nights,maximum_nights

SELECT available, COUNT(available) FROM Calendar GROUP BY(available)
-- ('t', 5795797), ('f', 6475556)

-- Calculate the percentage of listing availability
WITH a AS (
  SELECT available, COUNT(available) OVER() AS total, COUNT(available) OVER(PARTITION BY available) AS t
  FROM Calendar
)
SELECT available, t, total, t*1.0/total
FROM a
GROUP BY available, t, total
-- ('t', 5795797, 12271353, Decimal('0.472303013367'))
-- ('f', 6475556, 12271353, Decimal('0.527696986632'))

-- Count distint dates
SELECT COUNT(DISTINCT date) FROM Calendar
-- (388, )

-- Count the number of available/unavailable listings grouped by date
SELECT date, available, COUNT(available) FROM Calendar GROUP BY date, available ORDER BY date
-- Output saved to csv file. Chart created using Tableau Public viewable at https://public.tableau.com/app/profile/raymond.mutyaba/viz/AirbnbAvailability_16547132437280/AirbnbAvailabilitybyDayoftheWeek
-- 776 rows returned, first row: (datetime.date(2022, 3, 8), 't', 5259), second row (datetime.date(2022, 3, 8), 'f', 16477)

-- Get a list of dates ordered by number of available/unavailable listings
WITH a AS (
  SELECT date, available, COUNT(available) OVER(PARTITION BY date, available ORDER BY available) AS total FROM Calendar
)
SELECT date, available, total
FROM a
GROUP BY date, available, total
ORDER BY total
-- first row (datetime.date(2022, 6, 1), 't', 20814), second row (datetime.date(2022, 6, 2), 't', 20734), last row (datetime.date(2023, 3, 30), 't', 69)

-- Get a list of dates ordered by average adjusted_price
WITH a AS (
  SELECT date, available, COUNT(available) OVER(PARTITION BY date, available) AS total, AVG(adjusted_price) OVER(PARTITION BY date, available) AS average_price FROM Calendar
)
SELECT date, available, total, average_price
FROM a
GROUP BY date, available, total, average_price
ORDER BY average_price DESC
-- first row (datetime.date(2022, 3, 11), 't', 7310, Decimal('448.0800')), second row (datetime.date(2022, 3, 12), 't', 7304, Decimal('446.1182')), last row (datetime.date(2023, 3, 21), 'f', 7898, Decimal('210.9888'))
