-- 코드를 입력하세요
SELECT animal_id, i.name
from ANIMAL_INS i join ANIMAL_OUTS o using(ANIMAL_ID)
order by o.datetime-i.datetime desc limit 2;