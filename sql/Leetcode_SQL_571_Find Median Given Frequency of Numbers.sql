-- https://leetcode.com/problems/find-median-given-frequency-of-numbers/

SELECT 
	AVG(n3.Number) AS median
FROM (
	SELECT 
		n2.Number, n2.Frequency, n2.Counter, s1.SumFreq
	FROM (
		SELECT 
			n1.Number, n1.Frequency,
			(@freq := @freq + n1.Frequency) AS Counter
		FROM 
			Numbers n1, (SELECT @freq := 0) f
		ORDER BY n1.Number
		) n2, 
		(SELECT SUM(Frequency) AS SumFreq FROM Numbers) s1
	) n3
WHERE 
	n3.Counter BETWEEN (n3.SumFreq / 2) AND ((n3.SumFreq / 2) + n3.Frequency)
;