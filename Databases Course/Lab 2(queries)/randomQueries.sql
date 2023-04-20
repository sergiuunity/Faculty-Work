
    DECLARE @TODAY_DATE DATE;
  SET @TODAY_DATE = CAST(GETDATE() as date);

  --Delete the Exhibition that are no longer available as of today
  DELETE FROM Exhibition
  WHERE EndDate < @TODAY_DATE

  --DECLARE @TEST_DATE DATE;
  --SET @TEST_DATE = '2023-01-01';
  --DELETE FROM Exhibition
  --WHERE EndDate < @TEST_DATE

  INSERT into Exhibition VALUES
  (7, 'Example', NULL, '2022-01-01', '2022-12-30', 3)

  --DELETE The Exhibitions with a NULL Fee
  DELETE FROM Exhibition
  WHERE Fee IS NULL

  --Update the salary of the managers with salary in between 6000 and 6999 or whose name starts with 'D'
  UPDATE Manager
  Set Salary = 7000
  WHERE Salary BETWEEN 6000 AND 6999 OR Name LIKE 'D%'

  --All exhbitions available on the following Christmas Eve or New Year's Eve
  SELECT *
  FROM Exhibition
  WHERE '2022-12-24' BETWEEN StartDate AND EndDate
  UNION
  SELECT *
  FROM Exhibition
  WHERE '2022-12-31' BETWEEN StartDate AND EndDate


  --All exhibitions available today cheaper than 20
      DECLARE @TODAY1_DATE DATE;
  SET @TODAY1_DATE = CAST(GETDATE() as date);
  SELECT *
  FROM Exhibition
  WHERE Fee<20
  INTERSECT
  SELECT *
  FROM Exhibition
  WHERE @TODAY1_DATE BETWEEN StartDate AND EndDate

  --All exhibitions available today except those more expensive than 25
  DECLARE @TODAY2_DATE DATE;
  SET @TODAY2_DATE = CAST(GETDATE() as date);
  SELECT *
  FROM Exhibition
  WHERE @TODAY2_DATE BETWEEN StartDate AND EndDate
  EXCEPT
  SELECT *
  FROM Exhibition
  WHERE NOT Fee<25.00


  --INNER JOIN Manager, Museum, Exhibition
  SELECT 
  x.Name,
  y.Name,
  y.Location,
  z.Name,
  z.Fee
  FROM Manager x
  INNER JOIN 
  Museum y
  ON x.ManagerID = y.MuseumID
  INNER JOIN
  Exhibition z
  ON y.MuseumID=z.MuseumID
  ORDER BY z.Fee

  --LEFT JOIN Exhibit and ExhibitType
  SELECT
  e.ExhibitID,
  e.Name,
  e.Author,
  t.Type,
  t.TypeID
  FROM Exhibit e
  LEFT JOIN
  ExhibitType t
  ON e.TypeID=t.TypeID
  ORDER BY t.TypeID

    --RIGHT JOIN Manager and Museum
  SELECT *
  FROM Manager m1
  RIGHT JOIN
  Museum m2
  ON m1.ManagerID=m2.MuseumID
 
 --FULL JOIN Museum and Exhibition
 SELECT *
 FROM Museum m
 FULL JOIN
 Exhibition e
 ON m.MuseumID=e.MuseumID

 --Practice

 SELECT *
 FROM Exhibit a RIGHT JOIN ExhibitType b
 ON a.TypeID=b.TypeID

  SELECT *
 FROM ExhibitType a LEFT JOIN Exhibit b
 ON a.TypeID=b.TypeID

  SELECT *
 FROM Exhibit a RIGHT JOIN ExhibitType b
 ON a.TypeID=b.TypeID
 WHERE a.TypeID IS NULL

 SELECT *
 FROM Exhibit a FULL JOIN ExhibitType b
 ON a.TypeID=b.TypeID
 WHERE a.TypeID IS NOT NULL AND b.TypeID IS NOT NULL


 SELECT e.Fee, COUNT(*)
 FROM Exhibition e
 GROUP BY e.Fee

  SELECT DISTINCT e.Fee
 FROM Exhibition e

 SELECT *
 FROM Museum
 WHERE EXISTS
 (
 SELECT *
 FROM Museum
 WHERE Museum.Location LIKE 'K%'
 )

 INSERT into Exhibit VALUES
 (11, 'Pieta', 'Michelangelo', 4)

 INSERT into ExhibitExhibition VALUES
 (11,1)

  INSERT into Exhibit VALUES
 (12, 'Wings', 'Leonardo Da Vinci', 1)

 INSERT into ExhibitExhibition VALUES
 (12,1)

	SELECT OK
	FROM
	(SELECT 17 AS 'OK') BOSS
	GROUP BY OK
	HAVING SUM(OK)=(SELECT 18)

	  UPDATE Exhibition
  Set Fee = 18
  WHERE Name='The Splendours of Uzbekistan Oases'