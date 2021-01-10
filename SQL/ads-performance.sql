# Write your MySQL query statement below

WITH CTE AS (
             SELECT a.ad_id, SUM(CASE WHEN a.action = 'CLICKED' THEN 1
                                  ELSE 0 END) AS clicked,
                             SUM(CASE WHEN a.action = 'Viewed' THEN 1
                                  ELSE 0 END) AS viewed
             FROM Ads a
             GROUP BY a.ad_id
    )
    
SELECT CTE.ad_id, CASE WHEN CTE.clicked + CTE.viewed = 0 THEN 0.00
                       ELSE ROUND(100*(CTE.clicked)/(CTE.clicked+CTE.viewed) , 2) END AS ctr
FROM CTE
ORDER BY ctr DESC, CTE.ad_id ASC
