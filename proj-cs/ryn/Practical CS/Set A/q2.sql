CREATE TABLE students(Rollno INT PRIMARY KEY, Name VARCHAR(30), Age INT, Percentage INT);

INSERT INTO students VALUES(1, 'arun', 18, 65), (2, 'ankit', 19, 71), (3, 'Anu', 20, 80), (4,'Bala', 19, 67), (5, 'charan', 18, 95);

-- a)
SELECT * FROM students WHERE Percentage > 75;

-- b)
SELECT * FROM students WHERE Name LIKE '%n';

-- c)
SELECT COUNT(*) AS total_students, AVG(Percentage) AS average_marks FROM students;

-- d)
INSERT INTO students VALUES(6, "Karan", 19, 77);