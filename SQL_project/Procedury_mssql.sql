--procedure 1, dodaje nowego lekarza, jesli jego jeszcze niema w bazie
create procedure add_new_doc
	@Imie varchar(30),
	@Nazwisko varchar(30),
	@Adres varchar(30),
	@Numer varchar(30),
	@id_Specjalizacja varchar(30)

as
declare @Info varchar(60),
		@id_osoba int
begin
	if exists(select 1 from Osoba where Numer = @Numer and Imie = @Imie and Nazwisko = @Nazwisko)	
	begin	
		set @Info = 'Lekarz ' + @Imie + ' ' + @Nazwisko + ' juz jest zapisany w bazie.'  
	end
	else 
	begin	
		set @id_osoba = (select  max(id_Osoba) from Osoba) + 1
		insert into Osoba values (@id_osoba, @Imie, @Nazwisko, @Adres, @Numer)
		insert into Lekarz values (@id_osoba, @id_specjalizacja)
		set @Info = 'Lekarz ' + @Imie + ' ' + ' ' + @Nazwisko + ' zostal zapisany do bazy.'  
	end
	print @Info
end
go

exec add_new_doc	@Imie = 'Bob',
					@Nazwisko = 'Jadrowski',
					@Adres = 'Gorczewska 15',
					@Numer = 12345600,
					@id_Specjalizacja = 1

drop procedure add_new_doc

select * from Osoba
go

--procedure 2, moze sprawdzic, czy ktos z pacjentow ma dzisiaj urodziny lub wyswietlic kto i kiedy ich ma
create procedure birthday
	@t varchar(3)
	--gen or tod
as
declare curs cursor for (select id_Osoba, Imie, Nazwisko, Data_urodzenia from Osoba
						 inner join Pacjent on id_Osoba = id_Pacjent
						 where id_Osoba = id_Pacjent)
	declare @id_Osoba int, 
			@Imie varchar(30), 
			@Nazwisko varchar(30), 
			@Data_urodzenia date
open curs
fetch next from curs into @id_Osoba, @Imie, @Nazwisko, @Data_urodzenia
	
	begin
		if @t = 'tod'
		begin 
		print 'Dzisiaj maja urodziny:'
		select id_Osoba, Imie, Nazwisko, Data_urodzenia from Osoba
							 inner join Pacjent on id_Osoba = id_Pacjent
							 where id_Osoba = id_Pacjent and month(Data_urodzenia) = month(current_timestamp)
							 and day(Data_urodzenia) = day(current_timestamp)
				fetch next from curs into @id_Osoba, @Imie, @Nazwisko, @Data_urodzenia
		end
		else if @t = 'gen'
		begin 
		print 'Lista urodzin:'
		select id_Osoba, Imie, Nazwisko, Data_urodzenia from Osoba
							 inner join Pacjent on id_Osoba = id_Pacjent
							 where id_Osoba = id_Pacjent
		order by Data_urodzenia
		fetch next from curs into @id_Osoba, @Imie, @Nazwisko, @Data_urodzenia
		end
	end
close curs;
deallocate curs;
go

drop procedure birthday
exec birthday 'gen'

