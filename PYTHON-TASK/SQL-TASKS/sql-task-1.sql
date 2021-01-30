
WITH 
em_rank_tbl as (
SELECT
 employee_id ,
 first_name, 
 last_name,
 department_id ,
salary ,
 row_number() OVER (partition by employee_id ,department_id ORDER BY salary DESC) as salary_per_department_rank
 FROM employees
), 

salary_diff_tbl as (
SELECT t1.department_id , t1.employee_id ,t1.salary - t2.salary AS salary_diff
FROM em_rank_tbl as t1
JOIN em_rank_tbl as t2 
ON t1.salary_per_department_rank =  t2.salary_per_department_rank + 1
WHERE t1.salary_per_department_rank = 1 
) 

SELECT sdt.department_id , d.department_name , sdt.employee_id , e.first_name, e,last_name , sdt.salary_diff
FROM salary_diff_tbl sdt 
JOIN departments d
ON sdt.department_id = d.department_id
JOIN employees e
ON sdt.employee_id = employee_id