CREATE PROCEDURE dropOrganizerTable
AS
BEGIN
	DROP TABLE Organizer
	UPDATE Version
	SET CurrentVersion=2
END