# Leetcode 584. Find Customer Referee

- Link: https://leetcode.com/problems/find-customer-referee/


```MySQL
# Solution 1
SELECT
    name
FROM 
    customer
WHERE
    referee_id != 2
    OR referee_id IS NULL
;

# Solution 2
SELECT
    name
FROM 
    customer
WHERE 
    IFNULL(referee_id, 0) <> 2
;
```


