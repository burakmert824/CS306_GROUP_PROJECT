CREATE DATABASE project;
USE project;
CREATE TABLE countries (
	C_Code CHAR(32),
	C_Name CHAR(100),
	PRIMARY KEY (C_Code)
);
SELECT COUNT(*) FROM countries;
SELECT * FROM countries;
CREATE TABLE substance_use (
	C_Code CHAR(32) NOT NULL,
	YYear INTEGER,
	drugdeaths INTEGER,
	alcoholdeaths INTEGER,
	PRIMARY KEY (C_Code, YYear),
	FOREIGN KEY (C_Code)
	REFERENCES countries(C_Code)
	ON DELETE CASCADE
);
SELECT COUNT(*) FROM substance_use;
SELECT * FROM substance_use;
CREATE TABLE airpol_occure(
	C_Code CHAR(32) NOT NULL,
	deathcounts INTEGER,
	YYear INTEGER,
	Household_FosilFuel INTEGER,
	PRIMARY KEY (C_Code,YYear),
	FOREIGN KEY (C_Code)
	REFERENCES countries(C_Code)
	ON DELETE CASCADE
);
SELECT * FROM airpol_occure;
SELECT COUNT(*) FROM airpol_occure;
CREATE TABLE LifeExpact(
	C_Code CHAR(32) NOT NULL,
	YYear INTEGER,
	Life_ex_value DECIMAL(10,7),
	PRIMARY KEY (C_Code,YYear),
	FOREIGN KEY (C_Code) REFERENCES countries(C_Code) ON DELETE	CASCADE
);
SELECT * FROM LifeExpact;
SELECT COUNT(*) FROM LifeExpact;
CREATE TABLE Obesity_Report (
	C_Code CHAR(32) NOT NULL,
	YYear INTEGER,
	daily_calory INTEGER,
	prevalence_overweight DECIMAL(10,2),
	prevalence_obesity DECIMAL(10,2),
	death_rate DECIMAL(10,2),
	PRIMARY KEY (YYear, C_Code),
	FOREIGN KEY (C_Code) REFERENCES countries(C_Code) ON DELETE CASCADE
);
LOAD DATA LOCAL INFILE '/Users/ufukozdek/Downloads/CS306_GROUP_PROJECT-main/Obesity.csv'
INTO TABLE Obesity_Report
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(C_code, YYear, @daily_calory, @prevalence_overweight, @prevalence_obesity, @death_rate)
SET death_rate = IF(@death_rate = '', NULL, @death_rate), 
    prevalence_obesity = IF(@prevalence_obesity = '', NULL, @prevalence_obesity),
    prevalence_overweight = IF(@prevalence_overweight = '', NULL, @prevalence_overweight),
    daily_calory = IF(@daily_calory = '', NULL, @daily_calory);
 
SELECT COUNT(*) FROM Obesity_Report;
SELECT * FROM Obesity_Report;
CREATE TABLE Smoke_Examine(
	C_code CHAR(32) NOT NULL,
	YYear INTEGER,
	consumption_per_smoker_per_day DECIMAL(10,7),
	death_rate_per_100000_people DECIMAL(10,7),
	deaths INTEGER,
	share_of_adults_who_smoke DECIMAL(10,7),
	PRIMARY KEY (C_code, YYear),
	FOREIGN KEY (C_code) REFERENCES countries(C_code) ON DELETE	CASCADE
);

LOAD DATA LOCAL INFILE '/Users/ufukozdek/Downloads/CS306_GROUP_PROJECT-main/Smoking.csv'
INTO TABLE Smoke_Examine
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(C_code, YYear, consumption_per_smoker_per_day, @death_rate_per_100000_people, @deaths, share_of_adults_who_smoke)
SET deaths = IF(@deaths = '', NULL, @deaths), 
    death_rate_per_100000_people = IF(@death_rate_per_100000_people = '', NULL, @death_rate_per_100000_people);   

SELECT COUNT(*) FROM Smoke_Examine;
SELECT * FROM Smoke_Examine;