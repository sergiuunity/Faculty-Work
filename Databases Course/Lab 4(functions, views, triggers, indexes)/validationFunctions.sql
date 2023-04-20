USE [Art Galleries]
GO

--functions to validate

--validate a city/country
CREATE FUNCTION checkLocation(@loc varchar(50))
RETURNS bit AS
BEGIN
	DECLARE @valid bit
	IF @loc NOT LIKE '%[^A-Za-z ]%'
		SET @valid=1
	ELSE 
		SET @valid=0
	RETURN @valid
END
GO

DROP FUNCTION dbo.checkLocation
GO

PRINT dbo.checkLocation('Abc Def')
GO



--validate a Fee
CREATE FUNCTION checkFee(@fee money)
RETURNS bit AS
BEGIN
	DECLARE @valid bit
	IF @fee>=0
		SET @valid=1
	ELSE 
		SET @valid=0
	RETURN @valid
END
GO

DROP FUNCTION dbo.checkFee
GO

PRINT dbo.checkFee(5)
GO



--validate endDate>startDate
CREATE FUNCTION checkDates(@startDate date, @endDate date)
RETURNS bit AS
BEGIN
	DECLARE @valid bit
	IF @startDate<=@endDate
		SET @valid=1
	ELSE 
		SET @valid=0
	RETURN @valid
END
GO

DROP FUNCTION dbo.checkDates
GO

PRINT dbo.checkDates('2022-10-11','2022-10-10')
GO
