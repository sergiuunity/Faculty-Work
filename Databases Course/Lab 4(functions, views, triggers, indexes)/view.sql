--view containing all the museums, their manager, their exhibitions and the corresponding number of exhibits for each exhibition
CREATE VIEW museumsInfo
AS
		SELECT mus.Name AS 'Museum', mus.City, mus.Country, man.Name AS 'Manager', ExhibitionsAndTheirExhibits.Name AS 'Exhibition', ExhibitionsAndTheirExhibits.[No. of Exhibits]
	FROM
	(SELECT e.MuseumID, e.Name, x.ExhibitionID, (x.ExhibitionID) AS 'No. of Exhibits'
	FROM Exhibition e
	INNER JOIN ExhibitExhibition x ON e.ExhibitionID=x.ExhibitionID
	GROUP BY x.ExhibitionID, e.MuseumID, e.Name) ExhibitionsAndTheirExhibits
		INNER JOIN Museum mus ON mus.MuseumID=ExhibitionsAndTheirExhibits.MuseumID
		INNER JOIN Manager man ON mus.MuseumID=man.ManagerID
GO

SELECT * FROM museumsInfo

--show all the exhibits and their corresponding museum(and manager), having more than 3 exhibits
SELECT * FROM museumsInfo
WHERE [No. of Exhibits]>3

--drop table
DROP VIEW museumsInfo