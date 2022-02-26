# 1651. Hopper Company Queries III
* [Hopper Company Queries III - LeetCode](https://leetcode.com/problems/hopper-company-queries-iii/)

## Question
Write an SQL query to compute the average_ride_distance and average_ride_duration of every 3-month window starting from January - March 2020 to October - December 2020. Round average_ride_distance and average_ride_duration to the nearest two decimal places.


## Solution
### Recursive & Window founction 1

```SQL
with recursive month as ( 
    select 1 as month 
    union 
    select month + 1 as month 
    from month 
    where month < 12
)
select 
    month,
    round(avg(ride_distance)over(order by month rows between current row and 2 following), 2)as average_ride_distance, 
    round(avg(ride_duration)over(order by month rows between current row and 2 following), 2)as average_ride_duration
from(
    select 
        m.month, 
        case 
            when b.month is null then 0 
            else sum(b.ride_distance) end as ride_distance,
        case 
            when b.month is null then 0 
            else sum(b.ride_duration) end as ride_duration
    from month m 
    left join(
        select month(b.requested_at) as month,
            a.ride_distance,
            a.ride_duration 
        from AcceptedRides a 
        join Rides b on a.ride_id = b.ride_id 
        where year(b.requested_at) = '2020'
    ) b on m.month = b.month 
    group by m.month
) final_list
order by month
limit 10
```

### Recursive & Window founction 2

```SQL
WITH Month_Tbl AS(
    SELECT 1 AS 'month' 
    UNION ALL 
    SELECT month + 1 
    FROM Month_Tbl 
    WHERE month < 12
),
ride_info AS(
    SELECT MONTH(R.requested_at)AS 'month',
        SUM(A.ride_distance) AS 'monthly_distance',
        SUM(A.ride_duration) AS 'monthly_duration' 
    FROM AcceptedRides A 
    LEFT JOIN Rides R ON A.ride_id = R.ride_id 
    WHERE YEAR(R.requested_at) = 2020 
    GROUP BY MONTH(R.requested_at)
),
ride_all AS(
    SELECT M.month,
    CAST(ISNULL(R.monthly_distance, 0)AS FLOAT)AS 'monthly_distance',
    CAST(ISNULL(R.monthly_duration, 0)AS FLOAT)AS 'monthly_duration' FROM Month_Tbl M LEFT JOIN ride_info R ON M.month = R.month
)
SELECT TOP 10 month,
    ROUND(AVG(monthly_distance)OVER(ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING), 2) AS 'average_ride_distance',
    ROUND(AVG(monthly_duration)OVER(ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING), 2) AS 'average_ride_duration'
FROM ride_all
;
```