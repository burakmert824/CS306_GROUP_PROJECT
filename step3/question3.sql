

Select MAX(YYear) as max_year ,MIN(YYear) as min_year
from obesity_report;


delimiter //

CREATE PROCEDURE get_max_obesity_rate_of_country(IN iso_code VARCHAR(32))
BEGIN
    DECLARE death_rate_max FLOAT;
    DECLARE death_rate_year INT;
    DECLARE iso_code_count INT;
    
    SELECT COUNT(*) INTO iso_code_count FROM obesity_report WHERE C_Code = iso_code;
    -- eger o iso codde country bulamadiysan error ver
    IF iso_code_count = 0 THEN
        SELECT "Invalid parameter value" AS message;
    ELSE
		-- max death rateli columnu al yearini ve death_rate ini variablelera ata
		SELECT death_rate,YYear INTO death_rate_max, death_rate_year
			FROM obesity_report where C_code = iso_code 
			and death_rate =(SELECT MAX(death_rate) from obesity_report where C_code = iso_code);
		SELECT CONCAT('Maximum death rate of ',iso_code,': ', death_rate_max, ', Year: ', death_rate_year) AS message;
    END IF;
END//
delimiter ;

-- CALL THE PROCEDURE
CALL get_max_obesity_rate_of_country('AFG');
CALL get_max_obesity_rate_of_country('TUR');
CALL get_max_obesity_rate_of_country('kk');





