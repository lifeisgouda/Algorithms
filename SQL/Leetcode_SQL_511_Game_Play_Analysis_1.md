# Leetcode 511. Game Play Analysis 1

- [ ] Link: https://leetcode.com/problems/game-play-analysis-i/

## Answer
```SQL 
# Write your MySQL query statement below
SELECT  
    player_id
    , MIN(event_date) AS first_login
FROM 
    activity 
GROUP BY 
    1
```


![]()