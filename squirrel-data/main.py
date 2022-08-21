import pandas

sqr_data = pandas.read_csv("squirrel_data.csv")
fur_colors = sqr_data.PrimaryFurColor
gray_squirrels_count = len(sqr_data[sqr_data.PrimaryFurColor == "Gray"])
cinnamon_squirrels_count = len(sqr_data[sqr_data.PrimaryFurColor == "Cinnamon"])
black_squirrels_count = len(sqr_data[sqr_data.PrimaryFurColor == "Black"])

squirrels_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

squirrel_df = pandas.DataFrame(squirrels_dict)
squirrel_df.to_csv("squirrel_count")