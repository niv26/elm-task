-- site_visitors : date, site, number of visitors 
-- promotion_dates : start_date, end_date, site, promotion_code


WITH 
promotion_tbl as ( 
SELECT sv.date , sv.site , sv.num_of_visitors , coalesce(pd.promotion_code , 'N/A' ) AS promotion_code
FROM site_visitors sv 
LEFT JOIN promotion_dates pd 
ON pd.start_date >= sv.date AND pd.end_date <= sv.date 
),


SELECT ( promotion_date / regular_date ) * 100 
FROM (
    SELECT 
    SUM(CASE WHEN promotion_code <> 'N/A' THEN 1 ELSE 0) AS promotion_date,
    SUM(CASE WHEN promotion_code = 'N/A' THEN 1 ELSE 0) AS regular_date
    FROM promotion_tbl
)