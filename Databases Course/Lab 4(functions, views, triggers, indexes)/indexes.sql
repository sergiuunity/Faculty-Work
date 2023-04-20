INSERT INTO Exhibit VALUES
('Name', 'Francisco Goya', 1, NULL),
('Name', 'Francisco Goya', 1, NULL),
('Name', 'Francisco Goya', 1, NULL),
('Name', 'Francisco Goya', 1, NULL),
('Name', 'Francisco Goya', 1, NULL),
('Name', 'Francisco Goya', 1, NULL),
('Name', 'Francisco Goya', 1, NULL),
('Name', 'Francisco Goya', 1, NULL)

INSERT INTO Exhibit VALUES
('Name', 'Francis Adam', 1, NULL)

INSERT INTO ExhibitExhibition VALUES
(13, 1),
(14, 2),
(15, 11),
(16, 11),
(17, 12),
(18, 1),
(19, 1),
(20, 11),
(21, 12)


CREATE NONCLUSTERED INDEX N_idx_Exhibit_Author
ON Exhibit(Author);

DROP INDEX N_idx_Exhibit_Author
ON Exhibit


CREATE NONCLUSTERED INDEX N_idx_Exhibition_Dates
ON Exhibition(StartDate, EndDate);

DROP INDEX N_idx_Exhibition_Dates
ON Exhibition

--show all exhibitions having at least an exhibit from Francisco Goya, ordered by start & end date
SELECT Name, Fee, StartDate, EndDate
FROM Exhibition x
WHERE EXISTS
(SELECT x.ExhibitionID, y.ExhibitID, z.Author, z.Name
FROM ExhibitExhibition y
	INNER JOIN Exhibit z ON y.ExhibitID=z.ExhibitID
WHERE x.ExhibitionID=y.ExhibitionID AND z.Author='Francisco Goya')
ORDER BY StartDate, EndDate

-----
CREATE NONCLUSTERED INDEX N_idx_Exhibit_Author
ON Exhibit(Author);

SELECT Author
FROM Exhibit
WHERE Author='Francisco Goya'

DROP INDEX N_idx_Exhibit_Author
ON Exhibit



---


CREATE NONCLUSTERED INDEX N_idx_Exhibition_Fee
ON Exhibition(Fee);

SELECT *
FROM Exhibition
ORDER BY Fee


DROP INDEX N_idx_Exhibition_Fee
ON Exhibition