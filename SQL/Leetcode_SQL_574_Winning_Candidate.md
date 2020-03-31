# 574. Winning Candidate

- Link: https://leetcode.com/problems/winning-candidate/submissions/

## Answer
```SQL 
# Write your MySQL query statement below
SELECT
    name AS Name
FROM
    Candidate c
    INNER JOIN
    (
        SELECT
            Candidateid
        FROM
            Vote
        GROUP BY 
            Candidateid
        ORDER BY 
            COUNT(*) DESC
        LIMIT 1
    ) AS winner
WHERE
    c.id = winner.Candidateid
;
```
