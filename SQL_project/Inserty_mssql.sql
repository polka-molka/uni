INSERT INTO Gabinety VALUES (1, 'Okulista');
INSERT INTO Gabinety VALUES (2, 'Terapewta');
INSERT INTO Gabinety VALUES (3, 'Ortopeda');
INSERT INTO Gabinety VALUES (4, 'Neurolog');
INSERT INTO Gabinety VALUES (5, 'Kardiolog');

INSERT INTO Specjalizacja VALUES (1, 'Neurookulistyka');
INSERT INTO Specjalizacja VALUES (2, 'Infekcje wirusowe');
INSERT INTO Specjalizacja VALUES (3, 'Traumatologia');
INSERT INTO Specjalizacja VALUES (4, 'Neurologia');
INSERT INTO Specjalizacja VALUES (5, 'Zaburzenia serca');

INSERT INTO Medykament VALUES (1, 'Paracetamol', 'Przeciw boli');
INSERT INTO Medykament VALUES (2, 'Nospa', 'Przeciw spazmow');
INSERT INTO Medykament VALUES (3, 'Ulgix', 'Przeciw boli zoladku');
INSERT INTO Medykament VALUES (4, 'Tantum verde', 'Przeciw boli gardla');
INSERT INTO Medykament VALUES (5, 'Rutinoskorbin', 'Przeciw grypy');

INSERT INTO Choroba VALUES (1, 'Grypa');
INSERT INTO Choroba VALUES (2, 'Migrena');
INSERT INTO Choroba VALUES (3, 'Zatrucie');
INSERT INTO Choroba VALUES (4, 'Atak serca');
INSERT INTO Choroba VALUES (5, 'Astma');

INSERT INTO Osoba VALUES (1, 'Bob', 'Jadrowski', 'Gorczewska 15', 768398478);
INSERT INTO Osoba VALUES (2, 'Patryk', 'Ziemiak', 'Inflancka 45', 927367473);
INSERT INTO Osoba VALUES (3, 'Duglas', 'Jeziorski', 'Ordynacka 59', 129037477);
INSERT INTO Osoba VALUES (4, 'Slawomir', 'Dumski', 'Radzyminska 33', 342894267 );
INSERT INTO Osoba VALUES (5, 'Jack', 'Smalloy', 'Zabraniecka 76', 824678273);
INSERT INTO Osoba VALUES (6, 'Kuba', 'Bolonski', 'Krolewska 1', 872498928);
INSERT INTO Osoba VALUES (7, 'Marta', 'Numska', 'Wilcza 18', 929374650);
INSERT INTO Osoba VALUES (8, 'Aleks', 'Grzeczny', 'Polawska 90', 438477930);
INSERT INTO Osoba VALUES (9, 'Olga', 'Dworska', 'Jaworowska 2', 788987900);
INSERT INTO Osoba VALUES (10, 'Inga', 'Gredowska', 'Krymska 123', 233498489);

INSERT INTO Lekarz VALUES (1, 1);
INSERT INTO Lekarz VALUES (2, 2);
INSERT INTO Lekarz VALUES (3, 3);
INSERT INTO Lekarz VALUES (4, 4);
INSERT INTO Lekarz VALUES (5, 5);

INSERT INTO Grafik_pracy VALUES (1, 1, '2022-06-06 08:00:00', '2022-06-6 16:00:00', 1);
INSERT INTO Grafik_pracy VALUES (2, 2, '2022-06-06 08:00:00', '2022-06-6 20:00:00', 2);
INSERT INTO Grafik_pracy VALUES (3, 3, '2022-06-06 08:00:00', '2022-06-6 15:00:00', 3);
INSERT INTO Grafik_pracy VALUES (4, 4, '2022-06-06 08:00:00', '2022-06-6 16:00:00', 4);
INSERT INTO Grafik_pracy VALUES (5, 5, '2022-06-06 08:00:00', '2022-06-6 19:00:00', 5);

INSERT INTO Pacjent VALUES (6, 'm', '2002-04-20');
INSERT INTO Pacjent VALUES (7, 'k', '1999-12-03');
INSERT INTO Pacjent VALUES (8, 'm','1975-06-14');
INSERT INTO Pacjent VALUES (9, 'k', '1956-09-30');
INSERT INTO Pacjent VALUES (10, 'k', '1985-11-22');

INSERT INTO Wizyta VALUES (1, '2022-05-14', 6, 1, 2); 
INSERT INTO Wizyta VALUES (2, '2022-05-14', 7, 2, 2);
INSERT INTO Wizyta VALUES (3, '2022-04-05', 8, 3, 2);
INSERT INTO Wizyta VALUES (4, '2022-01-08', 9, 4, 5);
INSERT INTO Wizyta VALUES (5, '2022-02-22', 10, 5, 4);

INSERT INTO Recepta VALUES (1, 'Po jedzeniu', 1, 1);
INSERT INTO Recepta VALUES (2, 'Przed jedzeniem', 5, 2);
INSERT INTO Recepta VALUES (3, '3 razy na dobe', 1, 3);
INSERT INTO Recepta VALUES (4, 'W ciagu 5 dni', 3, 4);
INSERT INTO Recepta VALUES (5, 'Nie wiecej 2 pigulek', 3, 5);