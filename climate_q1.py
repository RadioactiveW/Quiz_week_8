import matplotlib.pyplot as plt
import sqlite3

# Using sqlite3, load climate.db; and show the data.
connection = sqlite3.connect(r".\climate.db")
cursor = connection.cursor()


def updateList(r, tempList):
    for l in r:
        tempList.append(l)


years = []
co2 = []
temp = []

sql_cmd1 = """
SELECT Year FROM ClimateData;
"""
cursor.execute(sql_cmd1)
res = cursor.fetchall()
updateList(res, years)

sql_cmd2 = """
SELECT CO2 FROM ClimateData;
"""
cursor.execute(sql_cmd1)
res = cursor.fetchall()
updateList(res, co2)

sql_cmd3 = """
SELECT Temperature FROM ClimateData;
"""
cursor.execute(sql_cmd1)
res = cursor.fetchall()
updateList(res, temp)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_1.png")
