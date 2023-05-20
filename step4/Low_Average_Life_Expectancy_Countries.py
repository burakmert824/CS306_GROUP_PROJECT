import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector


cnx = mysql.connector.connect(user='root',password='MySQLGoktug',host='localhost',database='project')

# Create a cursor
cursor = cnx.cursor()

# Execute the SQL query
query = 'SELECT * FROM high_life_exp_countries;'

#It assumes that we use step3 high_life_exp_countries view statement which was
"""
CREATE VIEW high_life_exp_countries AS
SELECT
    c.C_Name AS Country,
    AVG(l.Life_ex_value) AS Avg_Life_Expectancy
FROM countries c
JOIN LifeExpact l ON c.C_Code = l.C_Code
WHERE l.YYear BETWEEN 1990 AND 2012
GROUP BY c.C_Name
HAVING AVG(l.Life_ex_value) <= 60;
"""
cursor.execute(query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Access the country names and average life expectancies
countries = []
life_expectancies = []

for row in rows:
    country = row[0]  # Country name
    life_expectancy = row[1]  # Average life expectancy

    countries.append(country)
    life_expectancies.append(life_expectancy)

# Close the cursor and connection
query = 'SELECT * FROM high_life_exp_countries;'
cursor.close()
cnx.close()

sorted_data = sorted(zip(life_expectancies, countries))

# Extract the sorted values
sorted_life_expectancies, sorted_countries = zip(*sorted_data)

#created gradiant for coloring purpose 
gradient = np.linspace(0, 1, len(sorted_countries))

# Create a bar plot to visualize the data
plt.figure(figsize=(20, 10))
plt.scatter(sorted_countries, sorted_life_expectancies, c=gradient, cmap='hot')
plt.xlabel('Country')
plt.ylabel('Average Life Expectancy')
plt.title('Average Life Expectancy by Country')

# Rotate the x-axis labels if needed
plt.xticks(rotation=90)

# Display the plot
plt.savefig('Low_Average_Life_Expectancy_Countries.png')