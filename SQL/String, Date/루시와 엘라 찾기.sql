-- 내 풀이
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS
    WHERE 
    NAME='Lucy' OR 
    NAME='Ella' OR 
    NAME='Pickle' OR
    NAME='Rogan' OR 
    NAME='Sabrina' OR 
    NAME='Mitty';
-- IN 활용
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS
    WHERE NAME in ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty');