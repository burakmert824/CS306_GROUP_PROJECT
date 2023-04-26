SELECT
    c.C_Name AS Country,
    COUNT(s.YYear) AS NumberOfYears,
    AVG(s.consumption_per_smoker_per_day) AS Avg_Consumption_Per_Smoker_Per_Day,
    SUM(s.deaths) AS Total_Deaths,
    MIN(l.Life_ex_value) AS Min_Life_Expectancy,
    MAX(l.Life_ex_value) AS Max_Life_Expectancy
FROM countries c
JOIN Smoke_Examine s ON c.C_Code = s.C_code
JOIN LifeExpact l ON c.C_Code = l.C_Code AND s.YYear = l.YYear
WHERE s.YYear BETWEEN 1990 AND 2000
GROUP BY c.C_Name
HAVING AVG(s.consumption_per_smoker_per_day) > 10
ORDER BY Total_Deaths DESC;

-- her ulkenin hangi yilda max drug ratei var bakiyor ve 0 dan buyukse aliyor
SELECT s.C_Code, s.YYear, s.drugdeaths
FROM substance_use s
INNER JOIN (
    SELECT C_Code, MAX(drugdeaths) AS max_deaths
    FROM substance_use
    GROUP BY C_Code
    HAVING MAX(drugdeaths) > 0
) AS m
ON s.C_Code = m.C_Code AND s.drugdeaths = m.max_deaths;

-- her ulkenin hangi yilda min alchol ratei var bakiyor ve 0 dan buyukse aliyor
SELECT s.C_Code, s.YYear, s.alcoholdeaths
FROM substance_use s
INNER JOIN (
    SELECT C_Code, MIN(alcoholdeaths) AS min_deaths
    FROM substance_use
    GROUP BY C_Code
    HAVING MIN(alcoholdeaths) > 0
) AS m ON s.C_Code = m.C_Code AND s.alcoholdeaths = m.min_deaths;


SELECT COUNT(*) 
FROM (SELECT c.C_Code 
  FROM obesity_report ob, high_life_exp_countries hlec 
  JOIN countries c ON hlec.Country = c.C_Name
  WHERE c.C_Code = ob.C_Code and ob.YYear between 2000 and 2010
  GROUP BY hlec.Country 
  HAVING AVG(ob.death_rate) > 9.66
) as t;

-- 2000 ve 2010 arasinda avagare life expectancysi 75 den buyuk olan ulkeler arasinda obesity death rate i 9.66 dan kucuk olan ulkelerin sayisini verir
SELECT COUNT(*) AS num_countries
FROM (
  SELECT c.C_Code, AVG(ob.death_rate) AS avg_death_rate
  FROM countries c
  JOIN obesity_report ob ON c.C_Code = ob.C_code
  JOIN high_life_exp_countries hlec ON c.C_Name = hlec.Country
  WHERE ob.YYear BETWEEN 2000 AND 2010
  GROUP BY c.C_Code
  HAVING avg_death_rate > 9.66
) AS t;

-- 2000 ile 2010 arasinda air pollutionlari topluyor eger degerler 0 dan buyukse
SELECT c.C_Code, c.C_Name, SUM(a.deathcounts) AS total_deathcounts
FROM airpol_occure a
JOIN countries c ON c.C_Code = a.C_Code
WHERE a.YYear BETWEEN 2000 AND 2010
GROUP BY a.C_Code, c.C_Name
HAVING SUM(a.deathcounts) > 0;