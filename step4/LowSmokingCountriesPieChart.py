import mysql.connector
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from mysql.connector import errorcode
def connectionCreator():
    try:
        cnx = mysql.connector.connect(user='root',
                                    password = 'qweqweqwe',
                                    database='project')
        print('Connection oldu')
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
    else:
        cnx.close()
        return None

mydb = connectionCreator()
query = "SELECT c.C_Name AS Country, AVG(s.death_rate_per_100000_people) AS Avg_Death_Rate_Per_100k_People"+" FROM countries c"+" JOIN Smoke_Examine s ON c.C_Code = s.C_code"+" WHERE s.YYear BETWEEN 1990 AND 2012"+" GROUP BY c.C_Name"+" HAVING AVG(s.death_rate_per_100000_people) <= 60;"
# By sending your query along with the connector, 
# pandas can automatically read the incoming data and create a dataframe for it

df = pd.read_sql(query,mydb)

#close the connection
mydb.close() 



# Let's see the dataset's sample
print(df.head())
palette_color = sns.color_palette('bright')
plt.pie(x='Avg_Death_Rate_Per_100k_People', labels='Country', colors=palette_color,data = df, autopct='%.0f%%')
plt.xticks(rotation=360, fontsize=10)
plt.title('Low smoking death rate countries between 1990 and 2012')
# add this line to adjust subplot spacing

plt.savefig('Atries.png')
plt.show()
