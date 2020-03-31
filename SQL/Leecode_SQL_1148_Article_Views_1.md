- https://leetcode.com/problems/article-views-i/submissions/
- Leecode SQL 1148. Article Views 1

```MySQL 
SELECT
    DISTINCT author_id AS id
FROM 
    Views
WHERE 
    author_id = viewer_id
ORDER BY 
    id 
```

