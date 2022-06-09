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
