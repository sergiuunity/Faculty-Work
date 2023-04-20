CREATE PROCEDURE dropForeignKeyExhibitionOrganizer
AS
BEGIN
	ALTER TABLE Exhibition
	DROP CONSTRAINT fk_Exhibition_Organizer
	ALTER TABLE Exhibition
	DROP COLUMN OrganizerID
	UPDATE Version
	SET CurrentVersion=3
END