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
