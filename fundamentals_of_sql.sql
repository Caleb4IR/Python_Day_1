-- Task 1
SELECT title FROM movies;
SELECT director FROM movies;
SELECT title, director FROM movies;
SELECT title, year FROM movies;
SELECT * FROM movies

-- Task 2
SELECT * FROM movies WHERE id = 6;
SELECT * FROM movies WHERE years BETWEEN 2000 AND 2010;
SELECT * FROM movies WHERE years NOT BETWEEN 2000 AND 2010;
SELECT * FROM movies where id between 1 and 5;

-- Task 3
SELECT * FROM movies WHERE title LIKE '%Toy Story%';
SELECT * FROM movies WHERE director = 'John Lasseter';
SELECT title, director FROM movies WHERE director != 'John Lasseter';
SELECT * FROM movies WHERE title LIKE '%WALL%';

-- Task 4
SELECT DISTINCT director FROM movies ORDER BY director;
SELECT * FROM movies ORDER BY year DESC LIMIT 4;
SELECT * FROM movies ORDER BY title LIMIT 5;
SELECT * FROM movies ORDER BY title LIMIT 5 OFFSET 5;

-- Task 5
SELECT * FROM north_american_cities WHERE country = 'Canada';
SELECT * FROM north_american_cities WHERE country = 'United States' ORDER BY latitude DESC;
SELECT * FROM north_american_cities WHERE Longitude < (SELECT Longitude FROM north_american_cities WHERE City = 'Chicago') ORDER BY Longitude;
SELECT * FROM north_american_cities WHERE Country = 'Mexico' ORDER BY Population DESC LIMIT 2;
SELECT * FROM north_american_cities WHERE Country = 'United States' ORDER BY Population DESC LIMIT 2 OFFSET 2;

-- Task 6
SELECT * FROM movies INNER JOIN boxoffice on movies.id = boxoffice.movie_id;
SELECT * FROM movies INNER JOIN boxoffice on movies.id = boxoffice.movie_id WHERE international_sales > domestic_sales;
SELECT * FROM movies INNER JOIN boxoffice on movies.id = boxoffice.movie_id ORDER BY rating DESC;

-- Task 7
SELECT DISTINCT Building FROM Employees;
SELECT * FROM buildings;
SELECT distinct building_name, role
FROM buildings
LEFT JOIN employees on building_name = building;

-- Task 8
SELECT name, role FROM employees WHERE building IS NULL;
SELECT B.Building_name FROM Buildings B LEFT JOIN Employees E ON B.Building_name = E.Building WHERE E.Building IS NULL;

-- Task 9
SELECT m.Title,
       (b.Domestic_sales + b.International_sales) / 1000000 AS Combined_sales_in_millions
FROM Movies m JOIN Boxoffice b ON m.Id = b.Movie_id;
SELECT m.Title, (b.Rating * 10) AS Rating_in_percent FROM Movies m JOIN Boxoffice b ON m.Id = b.Movie_id;
SELECT * FROM Movies WHERE Year % 2 = 0;

-- Task 10
SELECT MAX(years_employed) FROM employees;
SELECT Role, AVG(Years_employed) AS Average_years_employed FROM Employees GROUP BY Role;
SELECT Building, SUM(Years_employed) AS Total_years_worked FROM Employees GROUP BY Building;

-- Task 11
SELECT COUNT(*) AS Number_of_artists FROM Employees WHERE Role = 'Artist';
SELECT Role, COUNT(*) AS Number_of_employees FROM Employees GROUP BY Role;
SELECT SUM(Years_employed) AS Total_years_employed FROM Employees WHERE Role = 'Engineer';

--Task 12
SELECT Director, COUNT(*) AS Number_of_movies_directed FROM Movies GROUP BY Director;

SELECT director, sum(domestic_sales + international_sales) as total_sales
FROM movies
    INNER JOIN boxoffice
        ON id = movie_id
GROUP BY director;

--Task 13
INSERT INTO movies VALUES (4,"Toy Story 4", "John Lasseter", 2024, 81)
INSERT INTO boxoffice
values(4,8.7,340000000,270000000);

-- Task 14
UPDATE movies
SET director = 'John Lasseter'
WHERE title = "A Bug's Life";
UPDATE movies
SET year = "1999"
WHERE title = "Toy Story 2";
UPDATE movies
SET title = "Toy Story 3", director = "Lee Unkrich"
WHERE title = "Toy Story 8";

-- Task 15
SELECT * FROM movies
WHERE year < 2005;
DELETE FROM movies
WHERE year < 2005;
SELECT * FROM movies
WHERE director = "Andrew Stanton";
DELETE FROM movies
WHERE director = "Andrew Stanton";

-- Task 16
CREATE TABLE IF NOT EXISTS Database (
    Name TEXT,
    Version FLOAT,
    Download_count INTEGER);

-- Task 17
ALTER TABLE movies
ADD Aspect_ratio FLOAT;
ALTER TABLE movies
ADD Language TEXT DEFAULT 'English';

-- Task 18
DROP TABLE movies;
DROP TABLE boxoffice;

SELECT player_id from player INNER JOIN player_skill_levels on player.player_skill_level = player_skill_levels.player_skill_level;
