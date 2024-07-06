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
CREATE OR REPLACE TRIGGER tr_Pacjent_insert
BEFORE INSERT
ON Pacjent
FOR EACH ROW
BEGIN
IF (EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM :NEW.Data_urodzenia)) > 100 THEN
RAISE_APPLICATION_ERROR(-20001,'Nie mo?na doda? pacjenta, kt?ry jest starszy ni? 100 lat.');
END IF;
END;
/

insert into Osoba values (123, 'www', 'www', 'w', 'ww');
insert into Pacjent values (123, 'k','10-10-1015');
select * from Pacjent;
delete from Pacjent where id_pacjent = 123;
delete from Osoba where id_osoba = 123;

ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MM-YYYY';