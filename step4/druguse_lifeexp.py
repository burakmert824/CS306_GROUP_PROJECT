import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='password',
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

# filter data for years between 1990 and 2012
filtered_data = data[(data['YYear'] >= 1990) & (data['YYear'] <= 2012)]

#take ratio off drug deaths an life exp
filtered_data['Ratio'] = filtered_data['drugdeaths'] / filtered_data['Life_ex_value']


filtered_data['YYear'] = filtered_data['YYear'].astype(int)

plt.figure(figsize=(8, 8))  # Adjust the width and height as needed

scatter = plt.scatter(filtered_data['Country_Name'], filtered_data['Ratio'], c=filtered_data['YYear'], cmap='viridis')
plt.xticks(rotation='vertical')
plt.xlabel('Country')
plt.ylabel('Ratio (Drug Deaths / Life Expectancy)')
plt.title('Ratio of Drug Deaths to Life Expectancy for high_drugdeaths_low_lifeex Countries')

cbar = plt.colorbar(scatter, label='Year')
cbar.set_ticks(filtered_data['YYear'].unique())

countries = filtered_data['Country_Name'].unique()
x_ticks = np.arange(len(countries))
x_labels = [country for country in countries]

#for dates in labels
for country in countries:
    country_data = filtered_data[filtered_data['Country_Name'] == country]
    first_year = country_data['YYear'].min()
    last_year = country_data['YYear'].max()
    date_label = f"{first_year}-{last_year}"
    x_idx = np.where(np.array(x_labels) == country)[0]
    if len(x_idx) > 0:
        x_labels[x_idx[0]] = f"{country}\n({date_label})"

plt.xticks(x_ticks, x_labels)

plt.tight_layout()
plt.show()
