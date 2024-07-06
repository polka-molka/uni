--trigger 1, nie dodaje pacjentow w wieku wiekszym niz 100
create trigger no_rep
on Pacjent
for insert
as begin 
	declare curs cursor for (select id_Osoba, Imie, Nazwisko, Data_urodzenia from Osoba
						 inner join Pacjent on id_Osoba = id_Pacjent
						 where id_Osoba = id_Pacjent)
	declare @id_Osoba int, 
			@Imie varchar(30), 
			@Nazwisko varchar(30), 
			@Data_urodzenia date
open curs
fetch next from curs into @id_Osoba, @Imie, @Nazwisko, @Data_urodzenia
	while @@fetch_status = 0
		begin
		if year(@Data_urodzenia) < year(current_timestamp) - 100
		begin
		rollback 
		print 'Not allowed to add people over 100 y.o.'
		end
	fetch next from curs into @id_Osoba, @Imie, @Nazwisko, @Data_urodzenia
	end
close curs;
deallocate curs;
end
go

insert into Osoba values (123, 'www', 'www', 'w', 'ww')
insert into Pacjent values (123, 'k','1000-10-10')

go

--trigger 2, zabiespicza wstawianie, usuwanie oraz apdejtowanie tabeli Gabinety
create trigger gab
on Gabinety
for insert, update, delete
as 

if exists (select 0 from inserted)
begin 
	if exists (select 0 from deleted)
			begin --u
				if exists (select 'X' from Gabinety 
							where Nazwa = (select Nazwa from inserted))
				begin
					rollback
					print('Such name already exists')
				end
			end
	else
			begin --i
				if exists (select 'X' from Gabinety a
							where Nazwa = (select Nazwa from Gabinety b))
				begin
					rollback
					print('The record already exists')
				end
			end
end
else
	begin --d
			print ('The room is deleted')
	end


drop trigger gab 
update Gabinety set Nazwa = 'Terapeuta' where Numer = 4
insert into Gabinety values (123, 'wwwww')
delete from Gabinety where Numer = 123
select * from Gabinety 