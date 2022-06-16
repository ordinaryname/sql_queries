"""
DOCKER
docker pull mcr.microsoft.com/mssql/server:2019-latest
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=yourStrong(!)Password" -p 1433:1433 --name mssql -d mcr.microsoft.com/mssql/server:2019-latest
docker ps -a
docker logs <container-id>
mssql -u sa -p <yourStrong(!)Password>
"""

"""
MS SQL
d.query('CREATE TABLE Listings(id nvarchar(max), listing_url nvarchar(max), scrape_id nvarchar(max), last_scraped nvarchar(max), name nvarchar(max), description nvarchar(max), neighborhood_overview nvarchar(max), picture_url nvarchar(max), host_id nvarchar(max), host_url nvarchar(max), host_name nvarchar(max), host_since nvarchar(max), host_location nvarchar(max), host_about nvarchar(max), host_response_time nvarchar(max), host_response_rate nvarchar(max), host_acceptance_rate nvarchar(max), host_is_superhost nvarchar(20), host_thumbnail_url nvarchar(max), host_picture_url nvarchar(max), host_neighbourhood nvarchar(max), host_listings_count nvarchar(max), host_total_listings_count nvarchar(max), host_verifications nvarchar(max), host_has_profile_pic nvarchar(20), host_identity_verified nvarchar(20), neighbourhood nvarchar(max), neighbourhood_cleansed nvarchar(max), neighbourhood_group_cleansed nvarchar(max), latitude nvarchar(max), longitude nvarchar(max), property_type nvarchar(max), room_type nvarchar(max), accommodates nvarchar(max), bathrooms nvarchar(max), bathrooms_text nvarchar(max), bedrooms nvarchar(max), beds nvarchar(max), amenities nvarchar(max), price nvarchar(max), minimum_nights nvarchar(max), maximum_nights nvarchar(max), minimum_minimum_nights nvarchar(max), maximum_minimum_nights nvarchar(max), minimum_maximum_nights nvarchar(max), maximum_maximum_nights nvarchar(max), minimum_nights_avg_ntm nvarchar(max), maximum_nights_avg_ntm nvarchar(max), calendar_updated nvarchar(max), has_availability nvarchar(20), availability_30 nvarchar(max), availability_60 nvarchar(max), availability_90 nvarchar(max), availability_365 nvarchar(max), calendar_last_scraped nvarchar(max), number_of_reviews nvarchar(max), number_of_reviews_ltm nvarchar(max), number_of_reviews_l30d nvarchar(max), first_review nvarchar(max), last_review nvarchar(max), review_scores_rating nvarchar(max), review_scores_accuracy nvarchar(max), review_scores_cleanliness nvarchar(max), review_scores_checkin nvarchar(max), review_scores_communication nvarchar(max), review_scores_location nvarchar(max), review_scores_value nvarchar(max), license nvarchar(max), instant_bookable nvarchar(20), calculated_host_listings_count nvarchar(max), calculated_host_listings_count_entire_homes nvarchar(max), calculated_host_listings_count_private_rooms nvarchar(max), calculated_host_listings_count_shared_rooms nvarchar(max), reviews_per_month nvarchar(max))', False)

'INSERT INTO Listings VALUES (CAST(? AS bigint), CAST(? AS nvarchar(4000)), CAST(? AS bigint), CAST(? AS date), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS bigint), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS date), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS varchar(10)), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS nvarchar(4000)), CAST(? AS varchar(10)), CAST(? AS varchar(10)), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS decimal(9,5)), CAST(? AS decimal(9,5)), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS bigint), CAST(? AS nvarchar(4000)), CAST(? AS nvarchar(4000)), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS nvarchar(4000)), CAST(? AS money), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS date), CAST(? AS varchar(10)), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS date), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS date), CAST(? AS date), CAST(? AS decimal(5,2)), CAST(? AS decimal(5,2)), CAST(? AS decimal(5,2)), CAST(? AS decimal(5,2)), CAST(? AS decimal(5,2)), CAST(? AS decimal(5,2)), CAST(? AS decimal(5,2)), CAST(? AS nvarchar(4000)), CAST(? AS varchar(10)), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS bigint), CAST(? AS decimal(11,7)))'

'INSERT INTO Listings VALUES (' + t + ')'

q = 'INSERT INTO Calendar VALUES (?,?,?,?,?,?,?)'

'INSERT INTO Listings VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

d.query('CREATE TABLE Calendar(listing_id nvarchar(max), date nvarchar(max), available nvarchar(20), price nvarchar(max), adjusted_price nvarchar(max), minimum_nights nvarchar(max), maximum_nights nvarchar(max))', False)

d.cursor.executemany(q,a)

d.query('ALTER TABLE Calendar ALTER COLUMN listing_id bigint', False)
d.query('ALTER TABLE Calendar ALTER COLUMN date date', False)
"""
