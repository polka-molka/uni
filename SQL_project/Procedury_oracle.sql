--procedure2
CREATE OR REPLACE PROCEDURE birthday (p_t VARCHAR2) AS
BEGIN
   IF p_t = 'tod' THEN
   begin
      DBMS_OUTPUT.PUT_LINE('Dzisiaj maja urodziny:');
      FOR cur_patient IN (SELECT id_Osoba, Imie, Nazwisko, Data_urodzenia
                         FROM Osoba
                         INNER JOIN Pacjent ON id_Osoba = id_Pacjent
                         WHERE EXTRACT(MONTH FROM Data_urodzenia) = EXTRACT(MONTH FROM SYSDATE) 
                         AND EXTRACT(DAY FROM Data_urodzenia) = EXTRACT(DAY FROM SYSDATE))
      LOOP
         DBMS_OUTPUT.PUT_LINE(cur_patient.id_Osoba || ' ' || cur_patient.Imie || ' ' || cur_patient.Nazwisko || ' ' || cur_patient.Data_urodzenia);
      END LOOP;
   end;

   ELSIF p_t = 'gen' THEN
   begin
      DBMS_OUTPUT.PUT_LINE('Lista urodzin:');
      FOR cur_patient IN (SELECT id_Osoba, Imie, Nazwisko, Data_urodzenia
                         FROM Osoba
                         INNER JOIN Pacjent ON id_Osoba = id_Pacjent
                         ORDER BY Data_urodzenia)
      LOOP
         DBMS_OUTPUT.PUT_LINE(cur_patient.id_Osoba || ' ' || cur_patient.Imie || ' ' || cur_patient.Nazwisko || ' ' || cur_patient.Data_urodzenia);
      END LOOP;
   end;
   END IF;
END;
/



EXEC birthday('gen');

--procedure2
CREATE OR REPLACE PROCEDURE get_patients_by_disease (p_disease_name IN VARCHAR2)
IS
  CURSOR c_patients IS
    SELECT Osoba.Imie, Osoba.Nazwisko
    FROM Pacjent
    JOIN Wizyta ON Pacjent.id_Pacjent = Wizyta.id_Pacjent
    JOIN Choroba ON Wizyta.id_Choroba = Choroba.id_Choroba
    JOIN Osoba ON Pacjent.id_Pacjent = Osoba.id_Osoba
    WHERE Choroba.Nazwa = p_disease_name;
  v_patient c_patients%ROWTYPE;
BEGIN
  OPEN c_patients;
  FETCH c_patients INTO v_patient;
  WHILE c_patients%FOUND 
  LOOP
    FETCH c_patients INTO v_patient;
  END LOOP;
  CLOSE c_patients;
END;
/
execute get_patients_by_disease ('Grypa')

SET ServerOutput ON