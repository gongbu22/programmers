-- 코드를 입력하세요
SELECT I.INGREDIENT_TYPE, SUM(F.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF F
JOIN ICECREAM_INFO  I USING(FLAVOR)
GROUP BY I.INGREDIENT_TYPE;