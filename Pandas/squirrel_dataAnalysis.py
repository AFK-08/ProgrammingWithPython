import pandas
data = pandas.read_csv("./Pandas/Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]

data = fur_color.value_counts()
data.to_csv("./Pandas/count_FurColors.csv")


