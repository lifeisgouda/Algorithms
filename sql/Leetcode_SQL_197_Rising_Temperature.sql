- https://leetcode.com/problems/rising-temperature/
- Leecode SQL 197. Rising Temperature

```MySQL
SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.RecordDate, w.RecordDate) = 1
        AND weather.Temperature > w.Temperature
;
```