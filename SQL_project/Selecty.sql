--zapytanie1 znajduje pacjentow, ktore byli chore na grype
select Imie, Nazwisko from Osoba o
inner join Pacjent p on o.id_Osoba = p.id_Pacjent
inner join Wizyta w on w.id_Pacjent = p.id_Pacjent
where id_Choroba = (select id_Choroba from Choroba where Nazwa = 'Grypa')

--zapytanie2 szuka lekarzy, ktore mieli wiecej niz 3 pacjenta
select Imie, Nazwisko from Osoba o
inner join Lekarz l on o.id_Osoba = l.id_Lekarz
where id_Lekarz in (select id_Lekarz from Wizyta
					group by id_Lekarz
					having count(*) > 3)

--zapytanie3 pozwala znalezc numer gabineta, w ktorym pracuje lekarz o danum indeksie
select Gabinet from Grafik_pracy gp
inner join Gabinety g on gp.Gabinet = g.Numer
where Gabinet = (select Gabinet from Grafik_pracy where id_Lekarz = 3)



