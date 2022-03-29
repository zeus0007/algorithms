SELECT OUTS.ANIMAL_ID, OUTS.NAME FROM ANIMAL_OUTS AS OUTS
    LEFT JOIN ANIMAL_INS AS INS
    ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
    WHERE INS.DATETIME > OUTS.DATETIME
    ORDER BY INS.DATETIME;