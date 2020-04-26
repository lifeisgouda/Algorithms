# Leetcode 512. Game Play Analysis 2

- Link: https://leetcode.com/problems/game-play-analysis-ii/



```MySQL
# Write your MySQL query statement below
SELECT 
    player_id
    , device_id 
FROM 
    Activity 
WHERE 
    (player_id, event_date) 
        IN (
                SELECT 
                    player_id, 
                    MIN(event_date) AS first_date 
                FROM 
                    Activity 
                GROUP BY 
                    1
            )
;
```


