CREATE PROCEDURE createOrganizerTable
AS
BEGIN
	CREATE TABLE Organizer(
		OrganizerID int NOT NULL PRIMARY KEY,
		Name varchar(50) NOT NULL,
		PhoneNumber varchar(15) NOT NULL
	);
	UPDATE Version
	SET CurrentVersion=3
END