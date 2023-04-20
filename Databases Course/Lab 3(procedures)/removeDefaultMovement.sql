CREATE PROCEDURE removeDefaultMovement
AS
BEGIN
	ALTER TABLE Exhibit
	DROP CONSTRAINT df_unknownMovement
	UPDATE Version
	SET CurrentVersion=1
END