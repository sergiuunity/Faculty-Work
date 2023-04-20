--Insert trigger for exhibit
CREATE TRIGGER ExhibitInsert on Exhibit
	AFTER INSERT
AS
BEGIN
	INSERT INTO Logs VALUES(GETDATE(), 'Insert', 'Exhibit', @@ROWCOUNT)
END
GO


INSERT INTO Exhibit VALUES
(21, 'ExhibitExample1', 'Author1', 1, 'ArtMovement1'),
(22, 'ExhibitExample2', 'Author2', 1, 'ArtMovement2'),
(23, 'ExhibitExample3', 'Author3', 1, 'ArtMovement3')
GO

SELECT * FROM Logs
GO





--Update trigger for exhibit
CREATE TRIGGER ExhibitUpdate on Exhibit
	AFTER UPDATE
AS
BEGIN
	INSERT INTO Logs VALUES(GETDATE(), 'Update', 'Exhibit', @@ROWCOUNT)
END
GO


UPDATE Exhibit
SET Author='newAuthorName'
WHERE ExhibitID>=20

SELECT * FROM Logs
GO





--Delete trigger for exhibit
CREATE TRIGGER ExhibitDelete on Exhibit
	AFTER DELETE
AS
BEGIN
	INSERT INTO Logs VALUES(GETDATE(), 'Delete', 'Exhibit', @@ROWCOUNT)
END
GO


DELETE FROM Exhibit
WHERE ExhibitID>=20

SELECT * FROM Logs
GO