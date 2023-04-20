--display all museums from France--x
SELECT Name, City, Country
FROM Museum
WHERE City='Paris' AND Country='France'

--display all the exhibitions that have exhibits from Da Vinci--x
	SELECT m.City, m.Country, m.Name, ExhibitionsExhibitsConnected.ExhibitionName
	FROM Museum m
	RIGHT JOIN
	(SELECT x.MuseumID, x.Name AS 'ExhibitionName' , z.Author
	FROM Exhibition x
		INNER JOIN ExhibitExhibition y ON x.ExhibitionID=y.ExhibitionID
		INNER JOIN Exhibit z ON y.ExhibitID=z.ExhibitID
	WHERE z.Author = 'Leonardo Da Vinci') ExhibitionsExhibitsConnected
	ON m.MuseumID=ExhibitionsExhibitsConnected.MuseumID

--show all the types of exhibits not present in the 'Hieroglyphs' exhibition--x
	SELECT Type
	FROM
	(SELECT z.TypeID
	FROM Exhibition x
		INNER JOIN ExhibitExhibition y ON x.ExhibitionID=y.ExhibitionID
		INNER JOIN Exhibit z ON y.ExhibitID=z.ExhibitID
	WHERE x.Name='Hieroglyphs') a
		RIGHT JOIN ExhibitType b ON a.TypeID=b.TypeID
	WHERE a.TypeID IS NULL

--show all the types of exhibits presented in a the 'Things' exhibition--x
	SELECT DISTINCT Type
	FROM
	(SELECT z.TypeID
	FROM Exhibition x
		INNER JOIN ExhibitExhibition y ON x.ExhibitionID=y.ExhibitionID
		INNER JOIN Exhibit z ON y.ExhibitID=z.ExhibitID
	WHERE x.Name='Things') a
		LEFT JOIN ExhibitType b ON a.TypeID=b.TypeID

--show all the exhibitions free today in London--x
	DECLARE @GIVEN_DATE1 DATE;
	SET @GIVEN_DATE1 = CAST(GETDATE() as date);
	SELECT m.Name, e.Name
	FROM Exhibition e INNER JOIN Museum m
	ON e.MuseumID = m.MuseumID
	WHERE @GIVEN_DATE1 BETWEEN e.StartDate AND e.EndDate AND m.City = 'London' AND m.Country='UK' AND e.Fee = 0

--show the number of exhibitions starting in 2022 in Paris--x
	SELECT COUNT(*) AS 'Number of exhibitions starting in 2022 in Paris'
	FROM Museum m
		INNER JOIN	Exhibition e1 ON m.MuseumID = e1.MuseumID
		INNER JOIN	ExhibitExhibition e2	ON e1.ExhibitionID = e2.ExhibitionID
		INNER JOIN	Exhibit e3	ON e2.ExhibitID = e3.ExhibitID
	WHERE e1.StartDate LIKE '2022-%' AND m.Name = 'Paris, France'

--show what is the name of the exhibition with most exhibits in the world and how many it has--x
	SELECT ExhibitionName, [No. of exhibits]
	FROM
	(SELECT ExhibitionName, COUNT(*) AS 'No. of exhibits'
	FROM
	(SELECT x.Name AS 'ExhibitionName', z.Name AS 'ExhibitName'
	FROM Exhibition x
		INNER JOIN ExhibitExhibition y ON x.ExhibitionID=y.ExhibitionID
		INNER JOIN Exhibit z ON y.ExhibitID=z.ExhibitID) subquery
	GROUP BY ExhibitionName) AllNoOfExhibits
	WHERE [No. of exhibits]=
	(SELECT MAX([No. of exhibits]) AS 'No. of exhibits'
	FROM
	(SELECT ExhibitionName, COUNT(*) AS 'No. of exhibits'
	FROM
	(SELECT x.Name AS 'ExhibitionName', z.Name AS 'ExhibitName'
	FROM Exhibition x
		INNER JOIN ExhibitExhibition y ON x.ExhibitionID=y.ExhibitionID
		INNER JOIN Exhibit z ON y.ExhibitID=z.ExhibitID) subquery
	GROUP BY ExhibitionName) AllNoOfExhibits)
	

--show the top 10 best paid managers working for a museum in Spain, in descending order--x
	SELECT TOP 10 m1.Name, m1.Salary
	FROM Manager m1 INNER JOIN Museum m2
	ON m1.ManagerID = m2.MuseumID
	WHERE m2.Country='Spain'
	ORDER BY Salary DESC

--show all museums having at least one exhibition with a fee higher than 20--x
	SELECT Name
	FROM Museum m
	RIGHT JOIN
	(SELECT MuseumID
	FROM Exhibition
	WHERE Fee>=20) AboveFee20Exhibitions
	on m.MuseumID=AboveFee20Exhibitions.MuseumID
	GROUP BY Name

--show the number of museums in UK--x
	SELECT COUNT(*) AS 'No. of museums in UK'
	FROM Museum
	WHERE Country='UK'

--show the average salary of an manager in France--x
	SELECT AVG(m2.Salary) AS 'Average Manager Salaray in France'
	FROM Museum m1 INNER JOIN Manager m2
	ON m1.MuseumID = m2.ManagerID
	WHERE m1.Country='France'

--show the price of going to all exhibitions from Le Louvre available on 24.12.2022--x
	SELECT SUM(Fee) AS 'Total'
	FROM
	(SELECT Fee
	FROM Museum m
	INNER JOIN
	(SELECT ExhibitionID, MuseumID, Fee
	FROM Exhibition
	WHERE '2022-12-24' BETWEEN StartDate AND EndDate) AvailableOnDate
	ON m.MuseumID=AvailableOnDate.MuseumID
	WHERE Name='Le Louvre') AllFees

--show all the museums having an average fee below the average fee of all exhibitions--x
	SELECT Name, [Average Fee]
	FROM
	(SELECT Name, AVG(Fee) AS 'Average Fee'
	FROM
	(SELECT m.Name, e.Fee
	FROM Museum m
		INNER JOIN Exhibition e
		ON m.MuseumID=e.MuseumID) MuseumsAndFees
	GROUP BY Name) EachMuseumAndAverage
	GROUP BY Name, [Average Fee]
	HAVING [Average Fee]<
	(SELECT AVG(Fee) AS 'Average Fee'
	FROM Exhibition)
	

--show how many exhibits are in each museum--x
	SELECT Name, COUNT(*) AS 'No. of exhibits'
	FROM
	Museum m
	INNER JOIN
	(SELECT x.MuseumID, x.Name AS 'ExhibitionName', z.Name AS 'ExhibitName'
	FROM Exhibition x
		INNER JOIN ExhibitExhibition y ON x.ExhibitionID=y.ExhibitionID
		INNER JOIN Exhibit z ON y.ExhibitID=z.ExhibitID) ExhibitionsExhibitsConnected
		ON m.MuseumID=ExhibitionsExhibitsConnected.MuseumID
	GROUP BY Name

--show all the artists that have their art in the 'The Tudors: Art and Majesty in Renaissance England' exhibition and how many exhibits they have in there--x
	SELECT Author, COUNT(Author) AS 'No. of exhibits'
	FROM
	(SELECT x.Name AS 'ExhibitionName' , z.Author, z.Name AS 'ExhibitName'
	FROM Exhibition x
		INNER JOIN ExhibitExhibition y ON x.ExhibitionID=y.ExhibitionID
		INNER JOIN Exhibit z ON y.ExhibitID=z.ExhibitID) ExhibitionsExhibitsConnected
	WHERE ExhibitionName='The Tudors: Art and Majesty in Renaissance England'
	GROUP BY Author
	
--EXTRA Queries to complete requirements

--show all the exhibitions ordered by their starting date & ending date--x
	SELECT Name, Fee, StartDate, EndDate
	FROM Exhibition
	ORDER BY StartDate, EndDate

--show all exhbitions available on the following Christmas Eve or New Year's Eve--x
	SELECT *
	FROM Exhibition
	WHERE '2022-12-24' BETWEEN StartDate AND EndDate
	UNION
	SELECT *
	FROM Exhibition
	WHERE '2022-12-31' BETWEEN StartDate AND EndDate

--show all exhibitions available today cheaper than 20--x
	DECLARE @TODAY1_DATE DATE;
	SET @TODAY1_DATE = CAST(GETDATE() as date);
	SELECT *
	FROM Exhibition
	WHERE Fee<20
	INTERSECT
	SELECT *
	FROM Exhibition
	WHERE @TODAY1_DATE BETWEEN StartDate AND EndDate

--show all exhibitions available today except those more expensive than 25--x
	DECLARE @TODAY2_DATE DATE;
	SET @TODAY2_DATE = CAST(GETDATE() as date);
	SELECT *
	FROM Exhibition
	WHERE @TODAY2_DATE BETWEEN StartDate AND EndDate
	EXCEPT
	SELECT *
	FROM Exhibition
	WHERE NOT Fee<25.00

--show all known managers and their corresponding museum--x
	SELECT m1.Name, m1.Salary, m2.Name AS 'Museum Name', m2.City, m2.Country
	FROM Manager m1 FULL JOIN Museum m2
	ON m1.ManagerID=m2.MuseumID

--show the museums having the manager with the lowest salary--x
	SELECT x.Name, x.City, x.Country, y.Salary
	FROM Museum X
	INNER JOIN
	(SELECT ManagerID, Salary
	FROM Manager
	WHERE Salary IN
	(SELECT MIN(Salary) AS 'Salary'
	FROM Manager m1 INNER JOIN Museum m2
	ON m1.ManagerID=m2.MuseumID))y
	ON x.MuseumID=y.ManagerID

--show all exhibitions having at least an exhibit from Michelangelo--x
	SELECT *
	FROM Exhibition x
	WHERE EXISTS
	(SELECT *
	FROM ExhibitExhibition y
		INNER JOIN Exhibit z ON y.ExhibitID=z.ExhibitID
	WHERE x.ExhibitionID=y.ExhibitionID AND z.Author='Michelangelo')

--show all the museums and the number of exhibitions they have, only if they have at least 2 exhibitions--x
	SELECT m.Name, COUNT(*) AS 'No. of exhibits'
	FROM Museum m
		INNER JOIN Exhibition e ON m.MuseumID=e.MuseumID
	GROUP BY m.Name
	HAVING COUNT(*)>=2

