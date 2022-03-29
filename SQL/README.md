# 프로그래머스 SQL
### SELECT
- 모든 레코드 조회하기
- 역순 정렬하기
- 아픈 동물 찾기
- 어린 동물 찾기
- 동물의 아이디와 이름
- 여러 기준으로 정렬하기
- 상위 n개 레코드

### SUM, MAX, MIN
- 최댓값 구하기
- 최솟값 구하기
- 동물 수 구하기
- 중복 제거하기

### GROUP BY
- 고양이와 개는 몇마리 있을까
- 동명 동물 수 찾기
- 입양 시각 구하기(1)
- 입양 시각 구하기(2)


### SQL Knowledge
- 테이블 고르기 : SELECT
    ```
    SELECT * FROM table_name;
    ```
- 정렬하기 : ORDER BY
    ```
    ORDER BY column_name;
    ```
- 순서 : ASC(작->큰), DESC(큰->작)
    ```
    ORDER BY column_name DESC;
    ```
- 그룹 짓기 : GROUP BY
    ```
    GROUP BY column_name;
    ```
- 개수 세기 : COUNT()
    ```
    SELECT COUNT(column_name) FROM table_name;
    ```
- DATETIME 다루기 : YEAR(), MONTH(), HOUR()
    ```
    SELECT HOUR(column_name) FROM table_name;
    ```
- LIMIT 1 -> 맨뒤에 써서 출력할 개수 구하기
    ```
    SELECT * FROM table_name LIMIT 3;
    ```
- 중복 제거 : DISTINCT
    ```
    SELECT COUNT(DISTINCT column_name) FROM table_name;
    ```
- WHERE : 그룹짓기 이전에 사용하는 조건식
    ```
    WHERE column_name > 3 AND column_name < 100;
    ```
- HAVING : 그룹지은 이후에 사용하는 조건식
    ```
    HAVING column_name > 3 AND column_name < 100;
    ```
- 최대/최소 : MIN(), MAX()
    ```
    MIN(column_name)
    MAX(column_name)
    ```
- 변수 선언 : SET @변수명 := 값
    ```
    SET @variable := 0
    ```
- UNION : 두개의 조회 결과 colunmn안에 합치기(중복 자동 제거)
    ```
    SELECT 1
    UNION 
    SELECT 2
    ```
- UNION ALL : 두개의 조회 결과 중복 고려하지 않고 전부 합친다.
- 가상 테이블 생성: WITH
    ```
    WITH new_table AS (
        SELECT 1
        UNION
        SELECT 2
    )
    ```
    - WITH 응용1 column_name 지정
        ```
        WITH new_table(column_name) AS (
            SELECT 1
            UNION
            SELECT 2
        )
        ```
    - WITH 응용2 column_name을 변수처럼 사용하기 (정확히는 table의 column을 가져다 쓰는것)
        - 예시 : 입양 시각 구하기(2)
    
- AS로 고른 값 컬럼명 변경하기
    ```
    SELECT column AS c FROM table;
    ```
- SELECT로 숫자 넣기
    ```
    SELECT 1,2,3;
    ```
    결과
    ![picture 1](../images/cba76439c76bd5e3175a61874b0cfdc76cd6fc41a99c4af1dd77787d2530d8dd.png)
- SELECT + UNION
    ```
    SELECT 1 UNION SELECT 2;
    ```
    결과
    ![picture 3](../images/519c4e47e301cf14c906b522101743eeb82f3e40b195b35bc8ee0249e25a97b5.png) 
- 아래와 같이 SELECT하는 대상에 다른 테이블의 값을 합치고 싶으면 한줄씩 가져와야한다.
    ```
    SELECT col1,(
        SELECT col2 FROM table2
        WHERE 조건
        ) FROM table1
    ```
    - 입양 시각 구하기(2) 참고
- 




