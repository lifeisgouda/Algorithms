# Leetcode 177. Nth Highest Salary



* [Nth Highest Salary - LeetCode](https://leetcode.com/problems/nth-highest-salary/)

```SQL 
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  RETURN (
    SELECT 
        DISTINCT Salary 
    FROM Employee
    ORDER BY 
        Salary DESC
    LIMIT 
        1 OFFSET M
  );
END
```



# PL/SQL 

- Procedural Language extension to SQL
- SQL의 확장된 개념으로 PL/SQL Block 내에서 SQLdml DML(데이터 조작어)문과 Query(검색어)문, 절차형 언어(IF, LOOP) 등을 하용하여 절차적 프로그래밍을 가능하게 한 트랜잭션 언어

