import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='',
                              host='localhost',
                              database='project')

cursor = cnx.cursor()

# to retrieve data from the high_drugdeaths_low_lifeex view
query = "SELECT s.C_Code, s.YYear, s.drugdeaths, s.Life_ex_value, c.C_Name FROM high_drugdeaths_low_lifeex s JOIN countries c ON s.C_Code = c.C_Code"
cursor.execute(query)

rows = cursor.fetchall()
cursor.close()
cnx.close()

data = pd.DataFrame(rows, columns=['C_Code', 'YYear', 'drugdeaths', 'Life_ex_value', 'Country_Name'])

# filter data for years between 2010 and 2023
filtered_data = data[(data['YYear'] >= 2010) & (data['YYear'] <= 2023)]

filtered_data['Ratio'] = filtered_data['drugdeaths'] / filtered_data['Life_ex_value']

plt.scatter(filtered_data['Country_Name'], filtered_data['Ratio'], c=filtered_data['YYear'], cmap='viridis')
plt.xticks(rotation='vertical')
plt.xlabel('Country')
plt.ylabel('Ratio (Drug Deaths / Life Expectancy)')
plt.title('Ratio of Drug Deaths to Life Expectancy for high_drugdeaths_low_lifeex Countries')
plt.colorbar(label='Year')

plt.tight_layout()
plt.show()
