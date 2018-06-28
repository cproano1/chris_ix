-- SQL Exercises
-- --------------------
-- Use the nobel database from class to answer the following questions.

-- 1. Select the nobel database.

USE nobel;

-- 2. List the tables.

SHOW TABLES;

-- 3. Select the first ten records from the laureate table.

SELECT *
FROM laureate
LIMIT 10;

-- 4. Find the birth and death dates for Albert Einstein.

SELECT birth_date, death_date
FROM laureate
WHERE name='Albert Einstein';

-- 5. Find the Nobel Laureates who died in 2015 and whose name begins with 'Y'.

SELECT name, death_date
FROM laureate
WHERE (death_date LIKE '2015%') AND (name LIKE 'Y%');

-- 6. Find the last three Nobel Laureates born in 1900.

SELECT name , birth_date
FROM laureate
WHERE (birth_date LIKE '1900%')
ORDER BY birth_date DESC
LIMIT 3;

-- 7. Find the number of Nobel Prizes awarded between 1950 and 1960.

SELECT(COUNT(year))
FROM prize
WHERE (year >= 1950) AND (year <= 1960);

-- 8. Find the number of Nobel Prizes awarded in each year.

SELECT year, COUNT(year) AS total_pyear
FROM prize
GROUP BY year;

-- 9. In which year was the greatest number of Nobel Prizes awarded?

SELECT year, COUNT(year) AS total_pyear
FROM prize
GROUP BY year
ORDER BY total_pyear DESC
LIMIT 1;

-- 10. What is the average number of Nobel Prizes awarded per year? Do we know how to do this yet?

SELECT COUNT(*)/COUNT(DISTINCT(year))
FROM prize;


-- 11. In which years were more than fifteen Nobel Prizes awarded?

SELECT year, COUNT(*) AS countP
FROM prize
GROUP BY year HAVING countP > 15;

-- 12. Who is the Nobel Laureate with the shortest name?

Select name, LENGTH(name) AS shortest
FROM laureate
ORDER BY shortest
LIMIT 1;

-- 13. Which Nobel Laureate had the longest life? You might need to use IFNULL().

SELECT name, IFNULL((YEAR(death_date) - YEAR(birth_date)), 0) AS age
FROM laureate
ORDER BY age DESC
LIMIT 1;

-- 14. Which year has the most women Nobel Laureates?

SELECT year, COUNT(*) AS most_women
FROM laureate
INNER JOIN prize
ON laureate.id = prize.laureate_id
WHERE sex = 'F'
GROUP BY year  
ORDER BY most_women DESC
LIMIT 1;

-- 15. Which category has the most women Nobel Laureates?

SELECT category, COUNT(*) AS most_wom_cat
FROM laureate
INNER JOIN prize
ON laureate.id = prize.laureate_id
WHERE sex = 'F' AND type = 'Individual'
GROUP BY category 
ORDER BY most_wom_cat DESC
LIMIT 1;

-- 16. What is the average number of Nobel Prizes awarded per year?

SELECT COUNT(*)/COUNT(DISTINCT(year))
FROM prize;

