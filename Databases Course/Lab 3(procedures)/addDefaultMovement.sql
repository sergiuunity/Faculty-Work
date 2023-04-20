CREATE PROCEDURE addDefaultMovement
AS
BEGIN
	ALTER TABLE Exhibit
	ADD CONSTRAINT df_unknownMovement DEFAULT 'Unknown'
	FOR ArtMovement
	UPDATE Version
	SET CurrentVersion=2
END