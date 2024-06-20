import pandas as pd


df = pd.read_csv("Habits.csv")
habits = df['Name'].tolist()


habit_displayed = {1: df.iloc[0,4], 2: df.iloc[1,4], 3: df.iloc[2,4], 4: df.iloc[3,4], 5: df.iloc[4,4], 6: df.iloc[5,4], 7: df.iloc[6,4], 8: df.iloc[7,4]}

lowest_id = None
for habit_id, display_status in habit_displayed.items(): # AI used here
    if display_status == False:  # Checks if habit slot is available
        if lowest_id is None or habit_id < lowest_id:
            lowest_id = habit_id
            print(lowest_id)