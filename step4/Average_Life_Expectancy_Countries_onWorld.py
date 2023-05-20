import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import mysql.connector

cnx = mysql.connector.connect(user='root', password='MySQLGoktug', host='localhost', database='project')
#I tried to show life ex on worldmap after listing lowest.
# Create a cursor
cursor = cnx.cursor()

# Execute the SQL query
query = 'SELECT * FROM all_average_life_exp_countries;'
#BEFORE Runing the code make sure you have created all_average_life_exp_countries view statement in your mysql
"""
CREATE VIEW all_average_life_exp_countries AS
SELECT
    c.C_Code AS Country_Code,
    c.C_Name AS Country,
    AVG(l.Life_ex_value) AS Avg_Life_Expectancy
FROM countries c
JOIN LifeExpact l ON c.C_Code = l.C_Code
WHERE l.YYear BETWEEN 1990 AND 2012
GROUP BY c.C_Code;

select * from all_average_life_exp_countries;
"""
cursor.execute(query)

# Fetch all the rows from the result
rows = cursor.fetchall()

# Access the country codes and average life expectancies
country_codes = []
life_expectancies = []

for row in rows:
    country_code = row[0]  # Country code
    life_expectancy = row[2]  # Average life expectancy

    country_codes.append(country_code)
    life_expectancies.append(float(life_expectancy))  # Convert to float


# Close the cursor and connection
cursor.close()
cnx.close()

# Load the shapefile for the world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge the life expectancies data with the world map data
data = pd.DataFrame({'Country_Code': country_codes, 'Avg_Life_Expectancy': life_expectancies})
world_data = world.merge(data, left_on='iso_a3', right_on='Country_Code', how='left')

# Define the color range and labels
color_range = [40, 50, 60, 70, 80]
color_labels = ['40-49', '50-59', '60-69', '70-79', '80-89']

# Plot the world map with colored countries
fig, ax = plt.subplots(figsize=(15, 10))
world_data.plot(column='Avg_Life_Expectancy', cmap='YlOrRd_r', linewidth=0.8, ax=ax, edgecolor='0.8', legend=False)

# Add color bar legend
sm = plt.cm.ScalarMappable(cmap='YlOrRd_r')
sm.set_array(life_expectancies)
cbar = plt.colorbar(sm, ax=ax, fraction=0.03, pad=0.04)
cbar.set_ticks(color_range)
cbar.set_ticklabels(color_labels)

# Set the title and axes labels
ax.set_title('Average Life Expectancy by Country')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Display the plot
plt.savefig('Average_Life_Expectancy_World_Map.png')
plt.show()
