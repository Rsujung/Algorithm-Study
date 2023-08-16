-- 코드를 입력하세요
SELECT a.TITLE, a.BOARD_ID, b.REPLY_ID, b.WRITER_ID, b.CONTENTS, 
left(b.CREATED_DATE, 10) as CREATED_DATE
from USED_GOODS_BOARD as a 
join USED_GOODS_REPLY as b
on a.board_id = b.board_id
where a.created_date like '2022-10-%'
order by b.created_Date asc, a.title asc;