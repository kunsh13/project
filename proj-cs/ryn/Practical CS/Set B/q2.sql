CREATE TABLE Books(
    BookID INT PRIMARY KEY,
    BName VARCHAR(20),
    Price INT,
    Author VARCHAR(30)
);

INSERT INTO Books VALUES(1001, 'C++', 250, 'Prakash');
INSERT INTO Books VALUES(1002, 'Java', 375, 'Sumita');
INSERT INTO Books VALUES(1003, 'Python', 575, 'Preethi');
INSERT INTO Books VALUES(1004, 'HTML', 200, 'Manoj');

-- a)
SELECT BName FROM Books WHERE Price < 300;

-- b)
ALTER TABLE Books ADD Discount INT;

-- c)
SELECT * FROM Books WHERE BName LIKE "Pr%";

-- d)
SELECT * FROM Books WHERE Price = (SELECT MIN(Price) FROM Books);
SELECT * FROM Books WHERE Price = (SELECT MAX(Price) FROM Books);
