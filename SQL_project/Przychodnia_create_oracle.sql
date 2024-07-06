-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-12-04 16:15:10.531

-- tables
-- Table: Choroba
CREATE TABLE Choroba (
    id_Choroba integer  NOT NULL,
    Nazwa varchar2(20)  NOT NULL,
    CONSTRAINT Choroba_pk PRIMARY KEY (id_Choroba)
) ;

-- Table: Gabinety
CREATE TABLE Gabinety (
    Numer integer  NOT NULL,
    Nazwa varchar2(20)  NOT NULL,
    CONSTRAINT Gabinety_pk PRIMARY KEY (Numer)
) ;

-- Table: Grafik_pracy
CREATE TABLE Grafik_pracy (
    id_Grafik integer  NOT NULL,
    Gabinet integer  NOT NULL,
    Pracuje_od timestamp  NOT NULL,
    Pracuje_do timestamp  NOT NULL,
    id_Lekarz integer  NOT NULL,
    CONSTRAINT Grafik_pracy_pk PRIMARY KEY (id_Grafik)
) ;

-- Table: Lekarz
CREATE TABLE Lekarz (
    id_Lekarz integer  NOT NULL,
    id_Specjalizacja integer  NOT NULL,
    CONSTRAINT Lekarz_pk PRIMARY KEY (id_Lekarz)
) ;

-- Table: Medykament
CREATE TABLE Medykament (
    id_Medykament integer  NOT NULL,
    Nazwa varchar2(20)  NOT NULL,
    Wskazanie_do_stosowania varchar2(20)  NOT NULL,
    CONSTRAINT Medykament_pk PRIMARY KEY (id_Medykament)
) ;

-- Table: Osoba
CREATE TABLE Osoba (
    id_Osoba integer  NOT NULL,
    Imie varchar2(20)  NOT NULL,
    Nazwisko varchar2(20)  NOT NULL,
    Adres varchar2(20)  NOT NULL,
    Numer varchar2(15)  NOT NULL,
    CONSTRAINT Osoba_pk PRIMARY KEY (id_Osoba)
) ;

-- Table: Pacjent
CREATE TABLE Pacjent (
    id_Pacjent integer  NOT NULL,
    Plec char(1)  NOT NULL,
    Data_urodzenia date  NOT NULL,
    CONSTRAINT Pacjent_pk PRIMARY KEY (id_Pacjent)
) ;

-- Table: Recepta
CREATE TABLE Recepta (
    id_Recepta integer  NOT NULL,
    Sposob_uzycia varchar2(20)  NOT NULL,
    id_Medykament integer  NOT NULL,
    id_Wizyty integer  NOT NULL,
    CONSTRAINT Recepta_pk PRIMARY KEY (id_Recepta)
) ;

-- Table: Specjalizacja
CREATE TABLE Specjalizacja (
    id_Specjalizacja integer  NOT NULL,
    Nazwa varchar2(20)  NOT NULL,
    CONSTRAINT Specjalizacja_pk PRIMARY KEY (id_Specjalizacja)
) ;

-- Table: Wizyta
CREATE TABLE Wizyta (
    id_Wizyta integer  NOT NULL,
    Data date  NOT NULL,
    id_Pacjent integer  NOT NULL,
    id_Choroba integer  NOT NULL,
    id_Lekarz integer  NOT NULL,
    CONSTRAINT Wizyta_pk PRIMARY KEY (id_Wizyta)
) ;

-- foreign keys
-- Reference: Grafik_pracy_Gabinety (table: Grafik_pracy)
ALTER TABLE Grafik_pracy ADD CONSTRAINT Grafik_pracy_Gabinety
    FOREIGN KEY (Gabinet)
    REFERENCES Gabinety (Numer);

-- Reference: Grafik_pracy_Lekarz (table: Grafik_pracy)
ALTER TABLE Grafik_pracy ADD CONSTRAINT Grafik_pracy_Lekarz
    FOREIGN KEY (id_Lekarz)
    REFERENCES Lekarz (id_Lekarz);

-- Reference: Lekarze_Kontakt (table: Lekarz)
ALTER TABLE Lekarz ADD CONSTRAINT Lekarze_Kontakt
    FOREIGN KEY (id_Lekarz)
    REFERENCES Osoba (id_Osoba);

-- Reference: Lekarze_Specjalizacja (table: Lekarz)
ALTER TABLE Lekarz ADD CONSTRAINT Lekarze_Specjalizacja
    FOREIGN KEY (id_Specjalizacja)
    REFERENCES Specjalizacja (id_Specjalizacja);

-- Reference: Lista_wizyt_Lekarz (table: Wizyta)
ALTER TABLE Wizyta ADD CONSTRAINT Lista_wizyt_Lekarz
    FOREIGN KEY (id_Lekarz)
    REFERENCES Lekarz (id_Lekarz);

-- Reference: Lista_wizyt_Lista_chorob (table: Wizyta)
ALTER TABLE Wizyta ADD CONSTRAINT Lista_wizyt_Lista_chorob
    FOREIGN KEY (id_Choroba)
    REFERENCES Choroba (id_Choroba);

-- Reference: Pacjenci_Kontakt (table: Pacjent)
ALTER TABLE Pacjent ADD CONSTRAINT Pacjenci_Kontakt
    FOREIGN KEY (id_Pacjent)
    REFERENCES Osoba (id_Osoba);

-- Reference: Recepta_Lista_medykamentow (table: Recepta)
ALTER TABLE Recepta ADD CONSTRAINT Recepta_Lista_medykamentow
    FOREIGN KEY (id_Medykament)
    REFERENCES Medykament (id_Medykament);

-- Reference: Wizyta (table: Recepta)
ALTER TABLE Recepta ADD CONSTRAINT Wizyta
    FOREIGN KEY (id_Wizyty)
    REFERENCES Wizyta (id_Wizyta);

-- Reference: Wizyta_Pacjent (table: Wizyta)
ALTER TABLE Wizyta ADD CONSTRAINT Wizyta_Pacjent
    FOREIGN KEY (id_Pacjent)
    REFERENCES Pacjent (id_Pacjent);

-- End of file.

