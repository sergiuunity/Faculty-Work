CREATE PROCEDURE addMuseum(@id int, @name varchar(50), @city varchar(50), @country varchar(50))
AS
BEGIN
	IF dbo.isIdInMuseum(@id)=0
		BEGIN
			IF dbo.checkLocation(@name)=1 AND dbo.checkLocation(@city)=1 AND dbo.checkLocation(@country)=1
				BEGIN
					INSERT INTO Museum VALUES (@id, @name, @city, @country)
				END
			ELSE
				PRINT 'The given data is invalid.'
		END
	ELSE
		PRINT 'Museum with such id already exists in the table.'
END
GO

EXEC [Art Galleries].dbo.addMuseum 10, 'Name', 'City', 'Country'
GO

DROP PROCEDURE addMuseum


--posibilitate: sa primesti doar mid si eid il faci tu gen urmatoru care ar veni, il extragi
CREATE PROCEDURE addExhibition(@eid int, @name varchar(50), @fee money, @startDate date, @endDate date, @mid int)
AS
BEGIN
	IF dbo.isIdInExhibition(@eid)=0
		BEGIN
			IF dbo.isIdInMuseum(@mid)=1
				BEGIN
					IF dbo.checkDates(@startDate, @endDate)=1 AND dbo.checkFee(@fee)=1
						BEGIN
							INSERT INTO Exhibition VALUES(@eid, @name, @fee, @startDate, @endDate, @mid)
						END
					ELSE
						PRINT  'The given data is invalid.'
				END
			ELSE
				PRINT 'There is no Museum with such id.'
		END
	ELSE
		PRINT 'Exhibition with such id already exists.'
END
GO

DROP Procedure addExhibition
GO

EXEC [Art Galleries].[dbo].[addExhibition] 12, 'Example Exhibition', 10, '2023-01-01', '2023-10-05', 1
GO
