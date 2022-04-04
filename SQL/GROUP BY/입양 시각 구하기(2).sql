-- sql 변수 활용 방식
SET @hour := -1;
SELECT (@hour := @hour + 1) AS HOUR, 
    (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) AS COUNT
    FROM ANIMAL_OUTS 
    WHERE @hour < 23;
-- group by 이렇게 하면 NULL 이 없어서 안된다.
WITH 
RECURSIVE new_table(col1) AS (
    SELECT 0
    UNION ALL
    SELECT col1+1 FROM new_table
    WHERE col1 < 23
),
HOUR_COUNT AS (
    SELECT HOUR(DATETIME) AS HOUR, 
    COUNT(DATETIME) AS COUNT FROM ANIMAL_OUTS 
    GROUP BY HOUR(DATETIME))

SELECT col1, IFNULL((
    SELECT HOUR_COUNT.COUNT FROM HOUR_COUNT 
    WHERE HOUR_COUNT.HOUR = col1), 0) FROM new_table;