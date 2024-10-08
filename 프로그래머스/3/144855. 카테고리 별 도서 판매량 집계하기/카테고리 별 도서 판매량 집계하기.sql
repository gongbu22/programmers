-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK JOIN BOOK_SALES
USING(BOOK_ID)
WHERE EXTRACT(YEAR FROM SALES_DATE) = 2022 AND
EXTRACT(MONTH FROM SALES_DATE)=1
GROUP BY CATEGORY
ORDER BY CATEGORY;