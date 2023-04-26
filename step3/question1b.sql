
SELECT Country
FROM high_life_exp_countries
UNION
SELECT Country
FROM low_death_rate_countries;

SELECT h.Country
FROM high_life_exp_countries h
LEFT JOIN low_death_rate_countries l ON h.Country = l.Country
WHERE l.Country IS NULL
UNION
SELECT l.Country
FROM high_life_exp_countries h
RIGHT JOIN low_death_rate_countries l ON h.Country = l.Country
WHERE h.Country IS NULL
UNION
SELECT h.Country
FROM high_life_exp_countries h
JOIN low_death_rate_countries l ON h.Country = l.Country;
