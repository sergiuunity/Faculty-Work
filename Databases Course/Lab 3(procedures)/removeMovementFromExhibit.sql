CREATE PROCEDURE removeMovementFromExhibit
AS
BEGIN
	ALTER TABLE Exhibit
	DROP COLUMN ArtMovement
	UPDATE Version
	SET CurrentVersion=0
END