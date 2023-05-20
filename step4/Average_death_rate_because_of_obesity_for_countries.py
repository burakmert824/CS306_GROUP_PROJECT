import mysql.connector
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from mysql.connector import errorcode
def connectionCreator():
    try:
        cnx = mysql.connector.connect(user='root',
                                    password = 'CS306database',
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
query = "SELECT c.C_Name, AVG(ob.death_rate) AS avg_deathrate" + " FROM obesity_report ob,countries c" + " WHERE c.C_Code = ob.C_Code and ob.YYear BETWEEN 1990 AND 2012"+" GROUP BY C_Name" + " ORDER BY avg_deathrate ASC"

# By sending your query along with the connector, 
# pandas can automatically read the incoming data and create a dataframe for it

df = pd.read_sql(query,mydb)

#close the connection
mydb.close() 

# Let's see the dataset's sample
print(df.head())
plt.figure(figsize=(24, 12))
sns.barplot(x='C_Name',y='avg_deathrate',data = df)
plt.xticks(rotation=90, fontsize=6)
plt.xlabel('Country Name')
plt.ylabel('Avgerage deathrate(%)')
plt.title('The average obesity-related death rate among countries')
#plt.tight_layout()  # add this line to adjust subplot spacing
plt.savefig('Average_death_rate_because_of_obesity_for_countries.png')
plt.show()
