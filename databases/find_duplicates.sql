SELECT Email
FROM users
GROUP BY Email
HAVING (COUNT(Email) > 1)
