CREATE PROCEDURE changeVersion
@newVersion int
AS
BEGIN
	IF @newVersion=(SELECT CurrentVersion From Version)
		PRINT 'The database is already at the given version.'
	ELSE
		IF @newVersion<0 OR @newVersion>4
			PRINT 'Such version does not exist for the database.'
		ELSE
			IF @newVersion<(SELECT CurrentVersion From Version)
				BEGIN
					IF (SELECT CurrentVersion From Version)=4
						EXEC dbo.dropForeignKeyExhibitionOrganizer
					IF (SELECT CurrentVersion From Version)>=3 AND @newVersion<3
						EXEC dbo.dropOrganizerTable
					IF (SELECT CurrentVersion From Version)>=2 AND @newVersion<2
						EXEC dbo.removeDefaultMovement
					IF @newVersion=0
						EXEC dbo.removeMovementFromExhibit
				END
			ELSE
				IF @newVersion>(SELECT CurrentVersion From Version)
					BEGIN
						IF (SELECT CurrentVersion From Version)=0
							EXEC dbo.addMovementToExhibit
						IF (SELECT CurrentVersion From Version)<=1 AND @newVersion>1
							EXEC dbo.addDefaultMovement
						IF (SELECT CurrentVersion From Version)<=2 AND @newVersion>2
							EXEC dbo.createOrganizerTable
						IF @newVersion=4
						EXEC dbo.createForeignKeyExhibitionOrganizer
					END
END
