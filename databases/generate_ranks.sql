# NB: Assumes db with ANSI SQL 99 compliance and access to windowing functions
#     Assumes rounding to 2 decimal point precision is acceptable
SELECT ROUND(Score::numeric,2) AS Score
    , ROW_NUMBER() OVER (ORDER BY Score DESC) AS RANK
FROM results
ORDER BY Score DESC
