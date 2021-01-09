# Write your MySQL query statement below

SELECT c.country_name, 
       (CASE WHEN AVG(w.weather_state) >= 25 THEN 'Hot'
            WHEN AVG(w.weather_state) <= 15 THEN 'Cold'
            ELSE 'Warm' END) AS weather_type
FROM Countries c
JOIN Weather w
ON c.country_id = w.country_id
WHERE LEFT(w.day, 7) = '2019-11'
GROUP BY c.country_id
