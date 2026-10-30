
-- 1. Create employee table
CREATE TABLE employees (
    Employee TEXT,
    Department TEXT,
    Salary INTEGER,
    Experience INTEGER
);

-- 2. Insert employee records
INSERT INTO employees VALUES
('Amit', 'IT', 35000, 1),
('Priya', 'HR', 30000, 2),
('Rahul', 'IT', 45000, 3),
('Sneha', 'Finance', 40000, 2),
('Neha', 'HR', 32000, 1),
('Karan', 'Finance', 50000, 4),
('Riya', 'IT', 55000, 5),
('Akash', 'Sales', 28000, 1),
('Pooja', 'Sales', 35000, 3),
('Om', 'Finance', 48000, 4);

-- 3. Display all employees
SELECT * FROM employees;

-- 4. Find employees with salary above 40000
SELECT * FROM employees
WHERE Salary > 40000;

-- 5. Calculate average salary
SELECT AVG(Salary) AS Average_Salary
FROM employees;

-- 6. Department-wise average salary
SELECT Department, AVG(Salary) AS Average_Salary
FROM employees
GROUP BY Department;

-- 7. Find highest salary
SELECT MAX(Salary) AS Highest_Salary
FROM employees;

-- 8. Sort employees by salary
SELECT * FROM employees
ORDER BY Salary DESC;
