  INSERT into Museum VALUES
  (1, 'Le Louvre', 'Paris', 'France'),
  (2, 'The Metropolitan Museum of Art', 'New York City', 'USA'),
  (3, 'The British Museum', 'London', 'UK'),
  (4, 'The State Hermitage Museum', 'Saint Petersburg', 'Russia'),
  (5, 'The Prado', 'Madrid', 'Spain')
  
  INSERT into Manager VALUES
  (1, 'Jean-Luc Martinez', 8000),
  (2, 'Daniel H. Weiss', 7500),
  (3, 'Hartwig Fischer', 10000),
  (4, 'Mikhail Piotrovsky', 6300),
  (5, 'Miguel Falomir Faus', 9200)

  INSERT into Exhibition VALUES
  (1, 'Things', 17, '2022-10-12', '2023-01-23', 1),
  (2, 'The Splendours of Uzbekistan Oases', 17, '2022-11-23', '2023-03-06', 1),
  (3, 'The Tudors: Art and Majesty in Renaissance England', 30, '2022-10-10', '2023-01-08', 2),
  (4, 'Hieroglyphs', 18, '2022-10-13', '2023-02-19', 3),
  (5, 'Nineteenth- and Twentieth-Century Tapestries', 19, '2019-09-18', '2022-12-30', 4),
  (6, 'Goya, San Bernardino de Siena', 24, '2022-02-15', '2023-02-19',5)
  
  INSERT into ExhibitType VALUES
  (1, 'Painting'),
  (2, 'Drawing'),
  (3, 'Printmaking'),
  (4, 'Sculpture'),
  (5, 'Ceramics'),
  (6, 'Photography'),
  (7, 'Rock'),
  (8, 'Tapestry')


  INSERT into Exhibit VALUES
  (1,'Nature morte avec pasteques', 'Luis Egidio Melendez', 1),
  (2, 'Pipes et vase à boire', 'Jean Baptiste Siméon Chardin', 1),
  (3, 'Queen Syuyumbika', 'Chingiz Akhmarov', 1),
  (4, 'Angel Bearing Candlestick', 'Benedetto da Rovezzano ', 4),
  (5, 'Elizabeth I (The Hampden Portrait)', 'George Gower', 1),
  (6, 'Rosetta Stone', 'Unknown', 7),
  (7, 'The Adoration of the Magi', 'Burne-Jones', 8),
  (8, 'The Third of May 1808', 'Francisco Goya', 1),
  (9, 'The Dog', 'Francisco Goya', 1)

  INSERT into ExhibitExhibition VALUES
  (1,1),
  (2,1),
  (3,2),
  (4,3),
  (5,3),
  (6,4),
  (7,5),
  (8,6),
  (9,6)
