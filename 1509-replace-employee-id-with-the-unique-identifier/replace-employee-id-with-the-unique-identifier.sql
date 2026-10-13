# Write your MySQL query statement below
select unique_id ,name from Employees as A left JOin EmployeeUNI as B on A.id=B.id;
