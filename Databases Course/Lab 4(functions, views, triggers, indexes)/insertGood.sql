USE [Art Galleries]
GO
CREATE PROCEDURE addMuseumAndExhibition(@museumName varchar(50), @city varchar(50), @country varchar(50), @exhibitionName varchar(50), @fee money, @startDate date, @endDate date)
AS
BEGIN
	IF dbo.checkDates(@startDate, @endDate)=1 AND dbo.checkFee(@fee)=1 
	AND dbo.checkLocation(@city)=1 AND dbo.checkLocation(@country)=1
		BEGIN
			INSERT INTO Museum VALUES (@museumName, @city, @country)
			DECLARE @mid int
			SET @mid = SCOPE_IDENTITY()
			INSERT INTO Exhibition VALUES(@exhibitionName, @fee, @startDate, @endDate, @mid)
		END
	ELSE
		PRINT 'The given data is invalid.'
END
GO

DROP PROCEDURE addMuseumAndExhibition
GO

EXEC [Art Galleries].dbo.addMuseumAndExhibition 'Carnavalet Museum', 'Paris', 'France', 'Regards du Grand Paris', 15, '2022-06-22', '2023-12-31'
GO
