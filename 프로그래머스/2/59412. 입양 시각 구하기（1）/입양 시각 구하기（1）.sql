-- 코드를 입력하세요
SELECT TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) AS HOUR, COUNT(ANIMAL_ID) AS COUNT
FROM ANIMAL_OUTS
WHERE TO_CHAR(DATETIME, 'HH24') BETWEEN 9 AND 19
GROUP BY TO_CHAR(DATETIME, 'HH24')
ORDER BY TO_CHAR(DATETIME, 'HH24');