SELECT SUBSTRING_INDEX('450 Fondren, Houston, TX', ' ', 1) AS street_number;
SELECT REGEXP_SUBSTR('450 Fondren, Houston, TX', '^[0-9]+') AS street_number;
select sum(cast(substring_index(address, ' ', 1) as unsigned)) from employee

-- Synatx of window fn
-- <func>(<params>) OVER (PARTITION BY <expr1> ..., ORDER BY <expr2>..., <Frame Definition>,...)
-- Aggregate func => SUM, COUNT, AVG
-- Lead or lag func => LEAD, lag
-- Rank Function => RANK, DENSE_RANK, PERCENT_RANK, ROW_NUMBER
e.g.:
SELECT 
    *, 
    SUM(sales) over (partition by sales_id) as sum_sales_by_id,
-- (21, '2022-05-03', 66, 277, 198),
-- (21, '2022-05-04', 45, 277, 243),
-- (22, '2022-05-07', 85, 300, 108),
-- (22, '2022-05-08', 54, 300, 162),
-- (22, '2022-05-09', 67, 300, 229),
-- (22, '2022-05-10', 71, 300, 300);