import pandas as pd


def read_csv(): 
    global df
    df = pd.read_csv("Habits.csv")
    print(df)
read_csv()


habit_name = {1: df.iloc[0,0], 2: df.iloc[1,0], 3: df.iloc[2,0], 4: df.iloc[3,0], 5: df.iloc[4,0], 6: df.iloc[5,0], 7: df.iloc[6,0], 8: df.iloc[7,0]}
habit_goal = {1: df.iloc[0,1], 2: df.iloc[1,1], 3: df.iloc[2,1], 4: df.iloc[3,1], 5: df.iloc[4,1], 6: df.iloc[5,1], 7: df.iloc[6,1], 8: df.iloc[7,1]}
habit_progress = {1: df.iloc[0,2], 2: df.iloc[1,2], 3: df.iloc[2,2], 4: df.iloc[3,2], 5: df.iloc[4,2], 6: df.iloc[5,2], 7: df.iloc[6,2], 8: df.iloc[7,2]}
habit_completed = {1: df.iloc[0,3], 2: df.iloc[1,3], 3: df.iloc[2,3], 4: df.iloc[3,3], 5: df.iloc[4,3], 6: df.iloc[5,3], 7: df.iloc[6,3], 8: df.iloc[7,3]}
habit_displayed = {1: df.iloc[0,4], 2: df.iloc[1,4], 3: df.iloc[2,4], 4: df.iloc[3,4], 5: df.iloc[4,4], 6: df.iloc[5,4], 7: df.iloc[6,4], 8: df.iloc[7,4]}
habit_checkbox = {1: df.iloc[0,5], 2: df.iloc[1,5], 3: df.iloc[2,5], 4: df.iloc[3,5], 5: df.iloc[4,5], 6: df.iloc[5,5], 7: df.iloc[6,5], 8: df.iloc[7,5]}


def write_csv(habit_id):
    df.iloc[(habit_id - 1),0] = habit_name[habit_id]
    df.iloc[(habit_id - 1),1] = habit_goal[habit_id]
    df.iloc[(habit_id - 1),2] = habit_progress[habit_id]
    df.iloc[(habit_id - 1),3] = habit_completed[habit_id]
    df.iloc[(habit_id - 1),4] = habit_displayed[habit_id]
    df.iloc[(habit_id - 1),5] = habit_checkbox[habit_id]
    df.to_csv('Habits.csv', index = False)

write_csv(1)