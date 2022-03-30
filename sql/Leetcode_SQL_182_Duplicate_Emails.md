# Leetcode 182. Duplicate Emails

- Link: [Duplicate Emails - LeetCode](https://leetcode.com/problems/duplicate-emails/)

## Answer

### MySQL
```SQL 
# MySQL
SELECT
    DISTINCT Email AS Email
FROM 
    (
    SELECT 
        Email
        , COUNT(*) AS cnt
    FROM 
        Person 
    GROUP BY 
        1
    ) AS stat
WHERE 
    cnt >= 2
;

# Having
SELECT 
	Email
FROM  
	Person
GROUP BY 
	Email
HAVING 
	COUNT(Email) > 1
;

```

### PostgreSQL
```SQL 
# Postresql
WIHT stat AS (
SELECT 
    Email
    , COUNT(*) AS cnt
FROM 
    Person 
GROUP BY 
    1
)
SELECT
    DISTINCT Email AS Email
FROM 
    stat
WHERE 
    cnt >= 2
;
```

![](https://github.com/lifeisgouda/Algorithms/blob/master/img/leetcode-submissions-detail-314798056-2020-03-22-17_35_27.png)

