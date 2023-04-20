CREATE PROCEDURE createForeignKeyExhibitionOrganizer
AS
BEGIN
	ALTER TABLE Exhibition
	ADD OrganizerID int
	ALTER TABLE Exhibition
	ADD CONSTRAINT fk_Exhibition_Organizer FOREIGN KEY(OrganizerID) REFERENCES Organizer(OrganizerID)
	UPDATE Version
	SET CurrentVersion=4
END