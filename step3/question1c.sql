SELECT h.Country
FROM high_life_exp_countries h
WHERE h.Country IN ( SELECT l.Country 
					 FROM low_death_rate_countries l );
                     
SELECT h.Country
FROM high_life_exp_countries h
WHERE EXISTS ( SELECT 1 
				FROM low_death_rate_countries l
				WHERE h.Country = l.Country);

