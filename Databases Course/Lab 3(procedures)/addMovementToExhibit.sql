CREATE PROCEDURE addMovementToExhibit
AS
BEGIN
	ALTER TABLE Exhibit
	ADD ArtMovement varchar(50)
	UPDATE Version
	SET CurrentVersion=1
END