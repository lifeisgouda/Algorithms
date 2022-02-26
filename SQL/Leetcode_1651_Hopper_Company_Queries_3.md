# 1651. Hopper Company Queries III
* [Hopper Company Queries III - LeetCode](https://leetcode.com/problems/hopper-company-queries-iii/)

## Question
Write an SQL query to compute the average_ride_distance and average_ride_duration of every 3-month window starting from January - March 2020 to October - December 2020. Round average_ride_distance and average_ride_duration to the nearest two decimal places.


## Solution
### Recursive & Window founction 1

```SQL
with recursive t as (
    select 1 month 
    union all 
    select month + 1 
    from t 
    where month < 12
)
,t2 as(
    select 
        sum(a.ride_distance) as sum_distance,
        sum(a.ride_duration) as sum_duration,
        month(r.requested_at) as month 
    from 
        acceptedrides a 
        join rides r using(ride_id)
    where 
        year(r.requested_at) = 2020 
    group by 
        month
)
select 
    t.month,
    round(avg(ifnull(t2.sum_distance, 0)) over(order by month rows between current row and 2 following), 2) as average_ride_distance,
    round(avg(ifnull(t2.sum_duration, 0))over(order by month rows between current row and 2 following), 2) as average_ride_duration
from t
left join t2 using(month)
limit 10
;
```

# Recursive
