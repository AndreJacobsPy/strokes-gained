from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import pandas as pd

# some variables to help run scraper with any url
URL: str = 'https://datagolf.com/historical-tournament-stats?event_id=464&year=2022'
TOURNAMENT_ID: int = 35
TOURNAMENT_NAME: str = "Fortinet Championship"
YEAR: int = 2021
LOCATION: str = "California"
row_to_skip: int = 73
row_to_end: int = 158

def main() -> None:
    driver = Chrome()
    driver.get(URL)

    data = []

    for row_num in range(3, row_to_end+1):
        if row_num == row_to_skip:
            continue

        row = []

        position = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[10]/div/div[{0}]/div[1]/span'.format(row_num)).text
        row.append(position)

        name = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[10]/div/div[{0}]/div[2]/span[1]/a".format(row_num)).text
        row.append(' '.join(name.split(' ')[::-1]))

        score = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[10]/div/div[{0}]/div[3]/span'.format(row_num)).text
        row.append(score)

        for i in range(5, 11):
            sg = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[10]/div/div[{0}]/div[{1}]'.format(row_num, i)).text
            row.append(sg)

        data.append(row)

    df = pd.DataFrame(data)

    with open('column_names.txt') as infile:
        df.columns = infile.readline().split(',')

    df['player_name'] = df['player_name'].apply(lambda x: x.title())
    df['score'] = df['score'].apply(lambda x: x.replace('E', '0')).astype(int)

    for col in df.columns:
        if 'sg' in col:
            df[col] = df[col].astype(float)

    # output data to strokes_gained.csv
    df["tournament_id"] = TOURNAMENT_ID
    # df.to_csv("strokes_gained.csv", mode="a", header=False, index=False)

    # output to tournament_data.csv
    new_row = pd.DataFrame([[TOURNAMENT_ID, TOURNAMENT_NAME, YEAR, LOCATION]])
    new_row.columns = ["tournament_id", "name", "year", "location"]

    # new_row.to_csv("tournament_data.csv", mode="a", header=False, index=False)
    print(data)

if __name__ == "__main__":
    main()