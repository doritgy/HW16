
"""1. Create/Drop table:
CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount
INTEGER);
=>creates a table named "shopping", with primary key of integer named "id", text field named "name" and
an integer field named "amount"
DROP TABLE shopping
=> erase the table all together, with it's structure
===================================================
2. Rename table:
ALTER table shopping RENAME to shopp
=> changes the name of the table to "shopp"
ALTER table shopp RENAME to shopping
=>back to name shopping
===============================================
3. Insert rows into table:
INSERT INTO shopping VALUES (1, 'Avokado', 5);
INSERT INTO shopping VALUES (2, 'Milk', 2);
INSERT INTO shopping VALUES (3, 'Bread', 3);
INSERT INTO shopping VALUES (4, 'Chocolate', 8);
INSERT INTO shopping VALUES (5, 'Bamba', 5);
INSERT INTO shopping VALUES (6, 'Orange', 10);
=>inserts 6 records into shopping table, with values as in "values", with primary keys 1 to 6
========================================================
4. Display table:
select * from shopping
=> displays all the records of table "shopping", with all the fields
============================================================
5. ?
SELECT id, name FROM shopping
=> displays only fields named "id" and "name" from all records in table shopping
===========================================================
6. ?
SELECT * FROM shopping WHERE amount > 5
=> displays the records with id: 4, 6 from shopping because their amount is greater than 5
SELECT * FROM shopping WHERE amount = 2
=> displays the records with id: 1, 3, 4, 5, 6  from shopping because their amount is greater than 2
SELECT * FROM shopping WHERE name LIKE 'Bamba'
=>displays record with id 5, because it's name is "bamba", like means "in"
=================================================
7. ?
DELETE from shopping WHERE name like 'Orange';
=> deletes record with id 6, because it's name is "orange"
===========================================================
8. ?
UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'
=>updates the name "bisli" instead of "bamba" in shopping table, id # 5
UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'
=>updates the amount to 1, in record with id # 2, where the name is "milk"
======================================================
9. ?
ALTER TABLE shopping ADD COLUMN maavar
=>adds a column to the table shopping, the column is named "maavar", the column is empty at the moment
===============================================================
10. ?
UPDATE shopping SET maavar=6 WHERE id=1;
=>updates the column "maavar" to 6 in the first record, where id # = 1
UPDATE shopping SET maavar=3 WHERE id=2;
=>updates the column "maavar" to 3 in the second record, where id # = 2
UPDATE shopping SET maavar=12 WHERE id=3;
=>updates the column "maavar" to 12 in the third record, where id # = 3
UPDATE shopping SET maavar=8 WHERE id=4;
=>updates the column "maavar" to 8 in the forth record, where id # = 4
UPDATE shopping SET maavar=5 WHERE id=5;
=>updates the column "maavar" to 5 in the fifth record, where id # = 5
===================================================================
11. ?
SELECT * FROM shopping WHERE amount > 1 AND maavar > 5
=>displays all fields of shopping, for records with id 1, 3, 4
SELECT * FROM shopping WHERE maavar BETWEEN 3 AND 5
=>displays all fields of shopping, for records with id 2, 5
==========================================================
12. ?
SELECT * FROM shopping ORDER BY maavar
displays records 2, 5, 1, 4, 3 in this order, after ordered the records by fiels "maavar"
SELECT * FROM shopping ORDER BY maavar DESC
displays records  3, 4, 1, 5, 2 in this order, after ordered in reverse way "descending"  by fiels "maavar"
===================================================
13. ?
CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO books VALUES (1, 'SQL PROGRAMMING');
INSERT INTO books VALUES (2, 'CSHARP PROGRAMMING');
DELETE FROM books;
=> creates the table named "books", inserts to it 2 records and then deletes the table all together
===========================================================
14. ?
SELECT COUNT(*)from shopping
SELECT MAX(amount) from shopping
SELECT AVG(amount) from shopping
SELECT MIN(amount) from shopping
=> displays the number of records in the table shopping
then displays the max amount in the table, the avg amount in the table and the minimal amoung
=====================================================
15. ?
INSERT INTO shopping VALUES (6, 'Onions', 3, 6);
INSERT INTO shopping VALUES (7, 'Orio', 1, 8);
Select maavar, COUNT(*)FROM shopping GROUP BY maavar
=>inserts into the table shopping 2 records of onions and orio
then displays the field "maavar", and then the number of records in shopping , grouped by the field maavar
explanation: the field maavar is grouped, there are 5 groupes:
3	1
5	1
6	2
8	2
12	1
one record with value 3, one record with value 5, two records with value 6, two records with value 8
and one record with value 12, the count displays the number of records in every group
===========================================================
16. ?
SELECT id AS "SECRET", name, amount, maavar FROM shopping
17. ?
Select maavar, COUNT(*)FROM shopping GROUP BY maavar HAVING COUNT(*)>1
18. ?
CREATE TABLE prices (id INTEGER PRIMARY KEY, price INTEGER);
INSERT INTO prices VALUES (1, 3);
INSERT INTO prices VALUES (2, 7);
INSERT INTO prices VALUES (3, 12);
INSERT INTO prices VALUES (4, 5);
INSERT INTO prices VALUES (5, 3);
INSERT INTO prices VALUES (6, 2);
INSERT INTO prices VALUES (7, 10);
SELECT s.id, s.name, s.amount, s.maavar, p.price FROM shopping s JOIN
prices p ON s.id=p.id
=>creates a new table "prices", with the fields "id", "price", I believe it's the same id
 as in shopping
 then updates the new table with 7 records with id's and prices
 then joins the two tables: shopping and prices according to the field id in both tables
 and displays the joined tables
 id  name  amount mavar, price
1	Avokado	5	   6	   3
2	Milk	1	   3	   7
3	Bread	3	  12	  12
4	Chocolate8	  8	       5
5	Bisli	5	  5	      3
6	Onions	3	  6	      2
7	Orio	1	  8	     10
==========================================================


מה מחושב בתוך SECRET ? 19.
SELECT s.id, s.name, s.amount, s.maavar, p.price, s.amount * p.price AS
"SECRET" FROM shopping s JOIN prices p ON s.id=p.id
=>display of the joined tables, with a new column named "secret", which ontains price multiple amount
=================================================================

20. ?
SELECT s.id, s.name, s.amount, s.maavar, p.price FROM shopping s JOIN
prices p ON s.id=p.id WHERE p.price = (SELECT MAX(price) FROM
prices)
displays the joined tables, but filtered for the records which have maximal prices,
it is price equal to the maximal price in the prices table
==========================================================

)2( פתור:

Students
ID (INTEGER)PRIMARY KEY NAME (TEXT) CITY (TEXT) BIRTH (INTEGER)
1 SHALOM TEL AVIV 1974
2 YURI RAANANA 1980
3 ANAT RISHON 1994
4 DANA REHOVOT 1990
5 OMER JERUSALEM 1987

GRADE

- כתוב את השאילתות ליצירת הטבלאות )ללא האיכלוס(
___________________________________________________________________
=>_create table students( id integer primary key, name text, city text, birth int)
insert into students values(1, "shalom", "tel aviv", 1651),
(2, "yuri", "raanana", 1980),
(3, "anat", "rishon" 1994),
(4, "dana", "rehovot", 1990),
(5, "omer", "jerusalem", 1987)
create table grades (id integer primary key, grade int)
insert into grades values(1, 95),(2, 70), (3, 85), (4, 99), (5, 91)

__________________________________________________________________
- כתוב שאילתא אשר מדפיסה את כל התלמידים ולכל תלמיד את הציון שהוא קיבל
=>  select s.id, s.name, s.city, s.birth, g.grade from students s join grades g
 on s.id = g.id
1	shalom	tel aviv	1651	95
2	yuri	raanana	1980	70
3	anat	rishon	1994	85
4	dana	rehovot	1990	99
5	omer	jerusalem	1987	91


 ___________________________________________________________________
___________________________________________________________________
- כתוב שאילתא אשר מחשבת את הממוצע הכיתתי
select avg(grade) from grades
88.0

___________________________________________________________________
- כתוב שאילתא להוספת עמודה EXCELLENT. כעת שים YES כאשר הציון גבוה מ90- אחרת שים NO
___________________________________________________________________
alter table grades add column "excelent"
UPDATE grades SET EXCELENT = CASE WHEN grade > 90 THEN 'yes' ELSE 'no'
___________________________________________________________________
- *כתוב שאילתא אשר מדפיסה את כל התלמידים ולכל תלמיד את הציון שהוא קיבל רק עבור
התלמידים אשר קיבלו מעל הממוצע

SELECT s.*, g.* FROM students s JOIN grades g ON s.id = g.id
WHERE g.grade > (SELECT AVG(grade) FROM grades);
1	shalom	tel aviv	1651	1	95	yes
4	dana	rehovot	1990	4	99	yes
5	omer	jerusalem	1987	5	91	yes

___________________________________________________________________
___________________________________________________________________
- * כתוב שאילתא אשר מדפיסה את התלמיד ואת ציונו עבור התלמיד אשר קיבל את הציון הגבוה
ביותר_______________________________________________________________
_______________________________________________________________

SELECT s.name, g.grade FROM students s JOIN grades g ON s.id = g.id
WHERE g.grade = (SELECT max(grade) FROM grades);

dana	99
"""

