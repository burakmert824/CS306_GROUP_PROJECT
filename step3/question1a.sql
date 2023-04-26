-- ulke codlari ve avarage obesity rateleri 
CREATE VIEW avg_obesity_rate as 
(SELECT ob.C_CODE, AVG(ob.death_rate) AS avg_deathrate
FROM obesity_report ob,countries c
WHERE c.C_Code = ob.C_Code and ob.YYear BETWEEN 2000 AND 2010
GROUP BY C_CODE);

Select * from avg_obesity_rate;

-- death countu 2500 den buyuk olup life expectancysi avaragedan kucuk olan ulkeler ve yillari
CREATE VIEW high_airpol_low_lifeex AS
SELECT a.C_Code, a.YYear, a.deathcounts, a.Household_FosilFuel
FROM airpol_occure a
INNER JOIN LifeExpact e ON a.C_Code = e.C_Code AND a.YYear = e.YYear
WHERE a.deathcounts > 2500 AND e.Life_ex_value < (SELECT AVG(Life_ex_value) FROM LifeExpact);

select * from high_airpol_low_lifeex;

-- life expectancysi avaragedan kucuk ve drug death 100den buyukse
CREATE VIEW high_drugdeaths_low_lifeex AS
SELECT s.C_Code, s.YYear, s.drugdeaths, e.Life_ex_value
FROM substance_use s
INNER JOIN LifeExpact e ON s.C_Code = e.C_Code AND s.YYear = e.YYear
WHERE s.drugdeaths > 100 AND e.Life_ex_value < (SELECT AVG(Life_ex_value) FROM LifeExpact);

select * from high_drugdeaths_low_lifeex;


-- This view shows the countries that have average life_exp over and equal to 75 from 1990 and 2012
CREATE VIEW high_life_exp_countries AS
SELECT
    c.C_Name AS Country,
    AVG(l.Life_ex_value) AS Avg_Life_Expectancy
FROM countries c
JOIN LifeExpact l ON c.C_Code = l.C_Code
WHERE l.YYear BETWEEN 1990 AND 2012
GROUP BY c.C_Name
HAVING AVG(l.Life_ex_value) >= 75;

select * from high_life_exp_countries;
-- shows the countries that have under 80 deaths per 100k people from smoking
CREATE VIEW low_death_rate_countries AS
SELECT c.C_Name AS Country,
    AVG(s.death_rate_per_100000_people) AS Avg_Death_Rate_Per_100k_People
FROM countries c
JOIN Smoke_Examine s ON c.C_Code = s.C_code
WHERE s.YYear BETWEEN 1990 AND 2012
GROUP BY c.C_Name
HAVING AVG(s.death_rate_per_100000_people) <= 80;
select * from low_death_rate_countries;