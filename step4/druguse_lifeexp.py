import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector


cnx = mysql.connector.connect(user='root',
                              password='Cnsn161N306',
                              host='localhost',
                              database='project')


cursor = cnx.cursor()

# Execute the SQL query to retrieve data from the high_drugdeaths_low_lifeex view
query = "SELECT s.C_Code, s.YYear, s.drugdeaths, s.Life_ex_value, c.C_Name FROM high_drugdeaths_low_lifeex s JOIN countries c ON s.C_Code = c.C_Code"
cursor.execute(query)

rows = cursor.fetchall()
cursor.close()
cnx.close()

# Create a pandas DataFrame from the fetched data
data = pd.DataFrame(rows, columns=['C_Code', 'YYear', 'drugdeaths', 'Life_ex_value', 'Country_Name'])

# Filter data for years between 2000 and 2010
filtered_data = data[(data['YYear'] >= 2010) & (data['YYear'] <= 2023)]

# Calculate the ratio of drug deaths to life expectancy for each country and year
filtered_data['Ratio'] = filtered_data['drugdeaths'] / filtered_data['Life_ex_value']


pivoted_data = filtered_data.pivot(index='Country_Name', columns='YYear', values='Ratio')

x = np.arange(len(pivoted_data))
country_names = pivoted_data.index

# Determine the number of years and generate corresponding colors
num_years = len(pivoted_data.columns)
colors = plt.cm.tab10(np.linspace(0, 1, num_years))

bar_width = 0.7 / num_years

for i, year in enumerate(pivoted_data.columns):
    ratios = pivoted_data[year]
    plt.bar(x + i * bar_width, ratios, width=bar_width, color=colors[i], label=year)

plt.xticks(x + (bar_width * (num_years - 1)) / 2, country_names, rotation='vertical')
plt.xlabel('Country')
plt.ylabel('Ratio (Drug Deaths / Life Expectancy)')
plt.title('Ratio of Drug Deaths to Life Expectancy for high_drugdeaths_low_lifeex Countries')

color_patches = [plt.Rectangle((0, 0), 1, 1, color=colors[i]) for i in range(num_years)]
plt.legend(color_patches, pivoted_data.columns, title='Year', loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()