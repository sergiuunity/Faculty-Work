--8 Procedures
EXEC [Art Galleries].dbo.addMovementToExhibit

EXEC [Art Galleries].dbo.addDefaultMovement

EXEC [Art Galleries].dbo.createOrganizerTable

EXEC [Art Galleries].dbo.createForeignKeyExhibitionOrganizer

EXEC [Art Galleries].dbo.dropForeignKeyExhibitionOrganizer

EXEC [Art Galleries].dbo.dropOrganizerTable

EXEC [Art Galleries].dbo.removeDefaultMovement

EXEC [Art Galleries].dbo.removeMovementFromExhibit

--Show CurrentVersion
SELECT CurrentVersion FROM [Art Galleries].dbo.Version

--Version Changing
DECLARE @newVersion int = 2

EXEC [Art Galleries].dbo.changeVersion @newVersion
