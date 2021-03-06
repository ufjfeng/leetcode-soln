/*
Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
*/
# Write your MySQL query statement below
SELECT DISTINCT a.Num AS ConsecutiveNums
FROM Logs AS a, Logs AS b, Logs AS c
WHERE b.Id - a.Id = 1 AND c.Id - b.Id = 1 AND a.Num = b.Num AND b.Num = c.Num
ORDER BY a.Num;
