
import pandas as pd

# import the data
df = pd.read_csv("strokes_data.csv")

# function for adding id column
def add_index(start: int, end: int, value: int) -> pd.DataFrame:
    data: pd.DataFrame = df[start:end].copy()
    data["tournament_id"] = value

    return data

# add index
first = add_index(0, 152, 1)

# add index for second tournament
second = add_index(152, 308, 2)

# add index for third tournament
third = add_index(308, 431, 3)

# add index for fourth tournament
fourth = add_index(431, 520, 4)

# add index for fifth tournament
fifth = add_index(520, 662, 5)

# add index for sixth tournament
sixth = add_index(662, 817, 6)

# add index for seventh tournament
seventh = add_index(817, 972, 7)

# add all data together
df = pd.concat([first, second, third, fourth, fifth, sixth, seventh])
print(df.head())

# exporting data to csv
df.to_csv("strokes_gained.csv", index=False)