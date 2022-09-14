import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrel_data)
data = squirrel_data[["Unique Squirrel ID", "Primary Fur Color"]]
# print(data)
count = data.groupby(by="Primary Fur Color", dropna=False).count()
# #
print(count)

another_count = squirrel_data.groupby(by="Primary Fur Color", dropna=False)["Primary Fur Color"].count()

print(another_count)

# data = pandas.read_csv("weather_data.csv")
# print(data.to_dict())
# average = sum(data["temp"]) / len(data["temp"])
# print(f"Average: {average}")
#
# max_temp = data["temp"].max()
# print(f"Maximum Temperature: {max_temp}")
# with open("weather_data.csv") as csv_file:
#     data = csv.DictReader(csv_file)
#     # print(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(row["temp"])
#     print(temperatures)


    # data = csv.reader(f)
    # next(data)
    # temperature = []
    # for row in data:
    #     temperature.append(row[1])
    # print(temperature)
