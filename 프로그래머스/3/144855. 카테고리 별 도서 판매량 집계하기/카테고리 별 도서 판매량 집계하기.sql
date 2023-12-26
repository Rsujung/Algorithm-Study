-- 코드를 입력하세요
SELECT book.CATEGORY, sum(book_sales.sales) as TOTAL_SALES
from book left join book_sales on book.book_id = book_sales.book_id
where month(book_sales.sales_date)=1
group by book.category
order by book.category asc;