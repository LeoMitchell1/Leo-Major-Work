import pandas as pd

cdf = pd.read_csv("Calendar.csv")

for i in range(10):
    for j in range(1,9):
                if cdf.iloc[(9-i), (j-1)] == "Health":
                    category = "#ffb3ba"
                elif cdf.iloc[(9-i), (j-1)] == "Fitness":
                    category = "#baffc9"
                elif cdf.iloc[(9-i), (j-1)] == "Learning":
                    category = "#bae1ff"
                elif cdf.iloc[(9-i), (j-1)] == "Finance":
                    category = "#ffffba"
                elif cdf.iloc[(9-i), (j-1)] == "Fun":
                    category = "#ffdfba"
                elif cdf.iloc[(9-i), (j-1)] == "Other":
                    category = "#eecbff"
                else:
                    category = "False"
                print(i, j, category)