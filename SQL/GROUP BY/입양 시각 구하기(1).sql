-- HAVING
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT FROM ANIMAL_OUTS
    GROUP BY HOUR
    HAVING HOUR >= 9 AND HOUR<20
    ORDER BY HOUR;
-- WHERE
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT FROM ANIMAL_OUTS
    WHERE (HOUR(DATETIME) >= 9 AND HOUR(DATETIME)<20)
    GROUP BY HOUR
    ORDER BY HOUR;