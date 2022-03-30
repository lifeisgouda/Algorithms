# mysql
# https://leetcode.com/problems/customers-who-never-order/

SELECT 
    Name AS Customers
FROM (
    SELECT
        c.Id
        , Name
        , CustomerID
    FROM 
        Customers AS c
        LEFT JOIN 
            Orders AS o ON o.CustomerID = c.Id
    WHERE
        CustomerID IS NULL
) AS List