# Leetcode 196. Delete Duplicate Emails
# https://leetcode.com/problems/delete-duplicate-emails/

# Solution 1
DELETE 
FROM 
	Person 
WHERE 
	Id NOT IN 
		(
		SELECT 
			id 
		FROM 
			(
			SELECT 
				MIN(Id) id 
			FROM  
				Person
			GROUP BY 
				Email
			) as _  
		)
;


# Solution 2
DELETE 
	P1
FROM 
	person P1, person P2
WHERE 
	P1.email = P2.email 
	AND P1.id > P2.id;
