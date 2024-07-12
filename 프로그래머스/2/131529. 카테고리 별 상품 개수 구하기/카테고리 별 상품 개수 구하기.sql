-- 코드를 입력하세요
SELECT substr(product_code, 1, 2), 
        count(substr(product_code, 1, 2)) from product
group by substr(product_code, 1, 2)
order by substr(product_code, 1, 2);