-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 
    CASE WHEN SEX_UPON_INTAKE like 'Neutered%' THEN 'O'
    WHEN SEX_UPON_INTAKE like 'Spayed%' then 'O'
    else 'X' end AS 중성화
FROM ANIMAL_INS
order by animal_id;
