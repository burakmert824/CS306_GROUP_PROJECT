-- finding maximum and minimum years of the countries
-- max = 2023
-- min = 0

-- add constraints
ALTER TABLE obesity_report
ADD CONSTRAINT check_year_range
CHECK (YYear BETWEEN 0 AND 2023);

-- insert after constraints and get error
INSERT INTO obesity_report (C_Code,YYear,daily_calory,prevalence_overweight,prevalence_obesity,death_rate)
VALUES ('AFG',-1,NULL,NULL,NULL,10);



-- delimeter bu multiline trigger fonksiyonunu yazmak icin gerekiyor icinde
-- ; kullanildigi icin yoksa hata veriyor
delimiter //
-- create trigger for inserting
CREATE TRIGGER fix_year_range_insert BEFORE INSERT ON obesity_report
FOR EACH ROW
BEGIN
  IF NEW.YYear < 0 THEN
    SET NEW.YYear = 0;
  ELSEIF NEW.YYear > 2023 THEN
    SET NEW.YYear = 2023;
  END IF;
END // 

-- create trigger for updating
CREATE TRIGGER fix_year_range_update
BEFORE UPDATE ON obesity_report
FOR EACH ROW
BEGIN
  IF NEW.YYear < 0 THEN
    SET NEW.YYear = 0;
  ELSEIF NEW.YYear > 2023 THEN
    SET NEW.YYear = 2023;
  END IF;
END //

delimiter ;
INSERT INTO obesity_report (C_Code,YYear,daily_calory,prevalence_overweight,prevalence_obesity,death_rate)
VALUES ('AFG',-1,NULL,NULL,NULL,10);