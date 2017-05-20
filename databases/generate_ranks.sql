SELECT ROUND(Score::numeric,2) AS Score
    , ROW_NUMBER() OVER (ORDER BY Score DESC) AS RANK
FROM results
ORDER BY Score DESC;
