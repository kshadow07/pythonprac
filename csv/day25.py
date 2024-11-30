# opening csv file with inbuilt csv module
# import csv
# with open("/Python/csv/weather_data.csv", "r") as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         # temp
#         print(row[1])

from operator import le
from numpy import average
import pandas

# data= pandas.read_csv("/Python/csv/weather_data.csv")
# monday=data[data.day=="Monday"]
# print(monday.temp[0]*(9/5)+32)

#Create a DataFrame 
# data={
#     "students":["Amy","James","Angela"],
#     "scores":[76,56,65]
    
# }

# newdata=pandas.DataFrame(data)
# jason=newdata.to_json()
# print(jason)

squireel_data=pandas.read_csv("/Python/csv/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_primary_fur=squireel_data[squireel_data.PrimaryFurColor=="Gray"]
cinemon_primary_fur=squireel_data[squireel_data.PrimaryFurColor=="Cinnamon"]
black_primary_fur=squireel_data[squireel_data.PrimaryFurColor=="Black"]

fur_data={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[len(grey_primary_fur),len(cinemon_primary_fur),len(black_primary_fur )]
}

print(pandas.DataFrame(fur_data).to_csv()) 