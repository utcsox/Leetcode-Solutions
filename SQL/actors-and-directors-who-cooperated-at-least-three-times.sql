# Write your MySQL query statement below

SELECT actor_id, director_id
FROM ActorDirector
GrOUP BY actor_id, director_id
Having COUNT(timestamp) >=3
