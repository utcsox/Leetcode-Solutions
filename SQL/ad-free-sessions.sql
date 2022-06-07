SELECT session_id
FROM Playback
WHERE session_id NOT IN
(SELECT session_id
FROM Playback P
INNER JOIN Ads A
ON P.customer_id = A.customer_id
AND A.timestamp BETWEEN P.start_time AND P.end_time)
