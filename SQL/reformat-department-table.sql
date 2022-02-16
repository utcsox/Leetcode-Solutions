
SELECT id,
SUM(CASE WHEN month = 'Jan' THEN d.revenue ELSE NULL END) AS Jan_Revenue,
SUM(CASE WHEN month = 'Feb' THEN d.revenue ELSE NULL END) AS Feb_Revenue,
SUM(CASE WHEN month = 'Mar' THEN d.revenue ELSE NULL END) AS Mar_Revenue,
SUM(CASE WHEN month = 'Apr' THEN d.revenue ELSE NULL END) AS Apr_Revenue,
SUM(CASE WHEN month = 'May' THEN d.revenue ELSE NULL END) AS May_Revenue,
SUM(CASE WHEN month = 'Jun' THEN d.revenue ELSE NULL END) AS Jun_Revenue,
SUM(CASE WHEN month = 'Jul' THEN d.revenue ELSE NULL END) AS Jul_Revenue,
SUM(CASE WHEN month = 'Aug' THEN d.revenue ELSE NULL END) AS Aug_Revenue,
SUM(CASE WHEN month = 'Sep' THEN d.revenue ELSE NULL END) AS Sep_Revenue,
SUM(CASE WHEN month = 'Oct' THEN d.revenue ELSE NULL END) AS Oct_Revenue,
SUM(CASE WHEN month = 'Nov' THEN d.revenue ELSE NULL END) AS Nov_Revenue,
SUM(CASE WHEN month = 'Dec' THEN d.revenue ELSE NULL END) AS Dec_Revenue

FROM  Department AS d
GROUP BY id
ORDER By id
