# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# temp_data = data["temp"].to_list()
# average_temp = data["temp"].mean()
# max_temp = data["temp"].max()
#
# max_temp_row = data[data.temp == data.temp.max()]
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)

import pandas

data_dict = {
    "students": ["Steve", "Bob", "Emma"],
    "scores": [85, 75, 95],
}

data = pandas.DataFrame(data_dict)
