> Write a SQL query to find all duplicate email addresses.

```
+--------+----------------------+
| Id     | Email                |
+--------+----------------------+
| 1234   | mpilgrim@example.com |
| 2534   | spilgrim@example.com |
| 36245  | mpilgrim@example.com |
+--------+----------------------+
```

The above table should give a result like this

```
+----------------------+
| Email                |
+----------------------+
| mpilgrim@example.com |
+----------------------+
```

[See solution](./find_duplicates.sql)

> Write a SQL query which given an arbitrary range will assign a unique rank to each rank in a column named Score.

```
+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
```

Given the above table, your query should generate the following report:

```
+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 2    |
| 3.85  | 3    |
| 3.65  | 4    |
| 3.65  | 5    |
| 3.50  | 6    |
+-------+------+
```

[See solution](./generate_ranks.sql)
