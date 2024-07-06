--trigger1
CREATE OR REPLACE TRIGGER tr_Pacjent_update
BEFORE UPDATE OR INSERT
ON Pacjent
FOR EACH ROW
BEGIN
IF updating then
IF :NEW.Data_urodzenia < :OLD.Data_urodzenia THEN
RAISE_APPLICATION_ERROR(-20001,'Nie mo?na zmieni? daty urodzenia na wcze?niejsz?.');
END IF;
END IF;
IF inserting THEN
IF EXTRACT(YEAR FROM :NEW.Data_urodzenia) > EXTRACT(YEAR FROM SYSDATE) THEN
RAISE_APPLICATION_ERROR(-20001,'Niepoprawna data urodzenia');
END IF;
END IF;
END;
/

select * from Pacjent;
update Pacjent set data_urodzenia = '20.04.34' where id_Pacjent = 6;
insert into Osoba values (123, 'www', 'www', 'w', 'ww');
insert into Pacjent values (123, 'k','10-10-2087');

--trigger2
CREATE OR REPLACE TRIGGER no_rep
BEFORE INSERT
ON Pacjent
FOR EACH ROW
BEGIN
DECLARE
id_Osoba INT;
Imie VARCHAR(30);
Nazwisko VARCHAR(30);
Data_urodzenia DATE;
BEGIN
SELECT id_Osoba, Imie, Nazwisko, Data_urodzenia
INTO id_Osoba, Imie, Nazwisko, Data_urodzenia
FROM Osoba
WHERE id_Osoba = :NEW.id_Pacjent;
    IF (EXTRACT(YEAR FROM Data_urodzenia) < EXTRACT(YEAR FROM SYSDATE) - 100) THEN
        RAISE_APPLICATION_ERROR(-20001, 'Not allowed to add people over 100 y.o.');
    END IF;
END;
END;
/
insert into Osoba values (123, 'www', 'www', 'w', 'ww');
insert into Pacjent values (123, 'k','10-10-1000');
select * from Pacjent;
delete from Pacjent where id_pacjent = 123;
delete from Osoba where id_osoba = 123;