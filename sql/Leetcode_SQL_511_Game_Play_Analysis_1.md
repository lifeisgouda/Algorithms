# Leetcode 511. Game Play Analysis 1

- Link: https://leetcode.com/problems/game-play-analysis-i/

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


![](https://github.com/lifeisgouda/Algorithms/blob/master/img/screencapture-leetcode-submissions-detail-314789968-2020-03-22-17_05_46.png)