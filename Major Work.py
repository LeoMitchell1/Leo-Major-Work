import customtkinter as custom
import tkinter as tk
import tkinter.messagebox as messagebox
import pandas as pd
from PIL import Image
from datetime import date
from datetime import timedelta


# Creates main app window
app = custom.CTk()
app.title("Habit Tracker")
app.geometry('660x690+600+130')
app.resizable(False, False)
custom.set_appearance_mode("Dark")
current_theme = custom.get_appearance_mode()
custom.set_default_color_theme("blue")  


# Reads the habits.csv file to receive all the saved data of each habit
def read_csv(): 
    global df
    df = pd.read_csv("Habits.csv")
read_csv() # Immediately reads the csv file upon opening the program

# Writes the data onto the habits.csv file to save any changes
def write_csv(habit_id):
    df.iloc[(habit_id - 1),0] = habit_name[habit_id]
    df.iloc[(habit_id - 1),1] = habit_goal[habit_id]
    df.iloc[(habit_id - 1),2] = habit_progress[habit_id]
    df.iloc[(habit_id - 1),3] = habit_completed[habit_id]
    df.iloc[(habit_id - 1),4] = habit_displayed[habit_id]
    df.iloc[(habit_id - 1),5] = habit_checkbox[habit_id]
    df.iloc[(habit_id - 1),6] = habit_category[habit_id]
    df.to_csv('Habits.csv', index = False)


# Initialises variables so they all are defined and have an initial value
habit_name = {1: df.iloc[0,0], 2: df.iloc[1,0], 3: df.iloc[2,0], 4: df.iloc[3,0], 5: df.iloc[4,0], 6: df.iloc[5,0], 7: df.iloc[6,0], 8: df.iloc[7,0]}
habit_goal = {1: df.iloc[0,1], 2: df.iloc[1,1], 3: df.iloc[2,1], 4: df.iloc[3,1], 5: df.iloc[4,1], 6: df.iloc[5,1], 7: df.iloc[6,1], 8: df.iloc[7,1]}
habit_progress = {1: df.iloc[0,2], 2: df.iloc[1,2], 3: df.iloc[2,2], 4: df.iloc[3,2], 5: df.iloc[4,2], 6: df.iloc[5,2], 7: df.iloc[6,2], 8: df.iloc[7,2]}
habit_completed = {1: df.iloc[0,3], 2: df.iloc[1,3], 3: df.iloc[2,3], 4: df.iloc[3,3], 5: df.iloc[4,3], 6: df.iloc[5,3], 7: df.iloc[6,3], 8: df.iloc[7,3]}
habit_displayed = {1: df.iloc[0,4], 2: df.iloc[1,4], 3: df.iloc[2,4], 4: df.iloc[3,4], 5: df.iloc[4,4], 6: df.iloc[5,4], 7: df.iloc[6,4], 8: df.iloc[7,4]}
habit_checkbox = {1: df.iloc[0,5], 2: df.iloc[1,5], 3: df.iloc[2,5], 4: df.iloc[3,5], 5: df.iloc[4,5], 6: df.iloc[5,5], 7: df.iloc[6,5], 8: df.iloc[7,5]}
habit_category = {1: df.iloc[0,6], 2: df.iloc[1,6], 3: df.iloc[2,6], 4: df.iloc[3,6], 5: df.iloc[4,6], 6: df.iloc[5,6], 7: df.iloc[6,6], 8: df.iloc[7,6]}
appearance_label = None
background = "#242424"
frame = "#2b2b2b"
gold = "#daa520"
full = False


# Category colours
health = "#ffb3ba"
fitness = "#baffc9"
learning = "#bae1ff"
finance = "#ffffba"
fun = "#ffdfba"
other = "#eecbff"


# Initialises all the lists for habit labels and buttons
habit_frames = []
name_labels = []
goal_labels = []
progress_labels = []
progress_bars = []
check_vars = []
complete_habit_buttons = []
edit_habit_buttons = []
delete_habit_buttons = []


# Function to find the lowest available habit id
def find_lowest_available_habit_id(): 
    global full
    full = False
    lowest_id = None
    for habit_id, display_status in habit_displayed.items(): 
        if display_status == False:  # Check if habit slot is available
            if lowest_id is None or habit_id < lowest_id:
                lowest_id = habit_id
                return lowest_id
    if lowest_id == None:
        messagebox.showerror("Error", "You have reached the maximum amount of habits.")
        return lowest_id


# Function for exit button
def exit_button():
    exit_confirm = custom.CTkToplevel(app)
    exit_confirm.title("Exit Confirmation")
    exit_confirm.geometry('250x120+900+500')
    exit_confirm.resizable(False, False)
    exit_confirm.attributes('-topmost', True)
    
    exit_label = custom.CTkLabel(master=exit_confirm,
                            text="Are you sure you want to exit?",
                            text_color="White")
    exit_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    yes_button = custom.CTkButton(master=exit_confirm,
                            text="Yes",
                            text_color="Black",
                            fg_color="Firebrick",
                            hover_color = "Orangered",
                            width = 80,
                            command=exit)
    yes_button.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

    no_button = custom.CTkButton(master=exit_confirm,
                            text="No",
                            text_color="Black",
                            width = 80,
                            command=exit_confirm.destroy)
    no_button.place(relx=0.3, rely=0.7, anchor=tk.CENTER)


# Function for the reset button
def reset_button():
    reset_confirm = custom.CTkToplevel(app)
    reset_confirm.title("Reset Confirmation")
    reset_confirm.geometry('250x120+900+500')
    reset_confirm.resizable(False, False)
    reset_confirm.attributes('-topmost', True)
    
    def reset_habits():
        for i in range(1,9):
            name_labels[i-1].grid_forget()
            goal_labels[i-1].grid_forget()
            progress_labels[i-1].grid_forget()
            progress_bars[i-1].grid_forget()
            complete_habit_buttons[i-1].grid_forget()
            edit_habit_buttons[i-1].grid_forget()
            delete_habit_buttons[i-1].grid_forget()
            habit_name[i] = "Habit " + str(i)
            habit_goal[i] = 0
            habit_progress[i] = 0
            habit_displayed[i] = False # Sets habit slot to available
            habit_completed[i] = False
            habit_checkbox[i] = False
            write_csv(i)
        reset_confirm.destroy()

    reset_label = custom.CTkLabel(master=reset_confirm,
                            text="Are you sure you want to reset?",
                            text_color="White")
    reset_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    yes_button = custom.CTkButton(master=reset_confirm,
                            text="Yes",
                            text_color="Black",
                            fg_color="Firebrick",
                            hover_color = "Orangered",
                            width = 80,
                            command=reset_habits)
    yes_button.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

    no_button = custom.CTkButton(master=reset_confirm,
                            text="No",
                            text_color="Black",
                            width = 80,
                            command=reset_confirm.destroy)
    no_button.place(relx=0.3, rely=0.7, anchor=tk.CENTER)


# Function for delete button
def delete_button(habit_id):
    name_labels[habit_id-1].grid_forget()
    goal_labels[habit_id-1].grid_forget()
    progress_labels[habit_id-1].grid_forget()
    progress_bars[habit_id-1].grid_forget()
    complete_habit_buttons[habit_id-1].grid_forget()
    edit_habit_buttons[habit_id-1].grid_forget()
    delete_habit_buttons[habit_id-1].grid_forget()
    habit_name[habit_id] = "Habit " + str(habit_id)
    habit_goal[habit_id] = 0
    habit_progress[habit_id] = 0
    habit_displayed[habit_id] = False # Sets habit slot to available
    habit_completed[habit_id] = False
    habit_checkbox[habit_id] = False
    write_csv(habit_id)
    

# Function for changing appearance
def change_appearance(mode:str):
    global appearance_menu, current_theme
    current_theme = mode
    custom.set_appearance_mode(mode)
    

# Function for settings button
def settings_button():
    global appearance_menu, current_theme
    app.withdraw()
    settings_window = custom.CTkToplevel(app)
    settings_window.title("Settings")
    settings_window.geometry('400x200+800+500')
    settings_window.resizable(False, False)
    settings_window.attributes('-topmost', True)

    appearance_label = custom.CTkLabel(master=settings_window,
                                        text="Appearance:")
    appearance_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    save_button = custom.CTkButton(master=settings_window,
                                    text="Save",
                                    text_color="Black",
                                    width=80,
                                    command = lambda: [app.deiconify(), settings_window.destroy()])
    save_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    appearance_menu = custom.CTkOptionMenu(settings_window,
                                values=["Dark", "Light", "System"],
                                command = change_appearance)
    appearance_menu.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    appearance_menu.set(current_theme)


# Function for updating habit progress
def update_progress(habit_id):
    checkbox = check_vars[habit_id-1].get()
    if checkbox == 'True':
        if (habit_progress[habit_id]) < int(habit_goal[habit_id]):
            habit_progress[habit_id] += 1
            habit_percentage = (habit_progress[habit_id]/int(habit_goal[habit_id]))
            progress_labels[habit_id-1].configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
            progress_bars[habit_id-1].set(habit_percentage)
            if habit_progress[habit_id] >= int(habit_goal[habit_id]):
                progress_labels[habit_id-1].configure(text="Completed!")
                habit_completed[habit_id] = True
        habit_checkbox[habit_id] = True
    if checkbox == 'False':
        if habit_progress[habit_id] > 0:
            habit_progress[habit_id] -= 1
            habit_percentage = (habit_progress[habit_id]/int(habit_goal[habit_id]))
            progress_labels[habit_id-1].configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
            progress_bars[habit_id-1].set(habit_percentage)
            if habit_progress[habit_id] < int(habit_goal[habit_id]):
                progress_labels[habit_id-1].configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
                habit_completed[habit_id] = False
        habit_checkbox[habit_id] = False
    write_csv(habit_id)


# Updates habit buttons and labels
def update_habit(habit_id):
    name_labels[habit_id-1].configure(text= str(habit_name[habit_id]))
    goal_labels[habit_id-1].configure(text="Goal: " + str(habit_goal[habit_id]) + "/w")
    progress_labels[habit_id-1].configure(text="Progress: " + str(habit_progress[habit_id]) + "%")
    progress_bars[habit_id-1].set(habit_progress[habit_id])
    write_csv(habit_id)
    

# Function for showing a new habit
def show_habit(habit_id):
    name_labels[habit_id-1].grid(row=0, column=0, padx=15, pady=(18, 5), sticky = "we")
    goal_labels[habit_id-1].grid(row=1, column=0, padx=15, pady=5,  sticky = "we")
    progress_labels[habit_id-1].grid(row=2, column=0, padx=15, pady=5,  sticky = "we")
    progress_bars[habit_id-1].grid(row=3, column=0, padx=15, pady=5,  sticky = "we")
    complete_habit_buttons[habit_id-1].grid(row=4, column=0, padx=(5,10), pady=5, sticky = "e")
    edit_habit_buttons[habit_id-1].grid(row=4, column=0, padx=(5,5), pady=5)
    delete_habit_buttons[habit_id-1].grid(row=4, column=0, padx=(15,0), pady=5, sticky = "w")


# Initially displays all the habits that were previously open
def initial_open():
    for i in range(1,9):
        if habit_displayed[i] == True:
            if habit_progress[i] == 0 and habit_goal[i] == 0:
                habit_percentage = 0
                progress_labels[i-1].configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
                progress_bars[i-1].set(habit_percentage)
            else:
                habit_percentage = (habit_progress[i]/int(habit_goal[i]))
                progress_labels[i-1].configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
                progress_bars[i-1].set(habit_percentage)
                if habit_progress[i] >= int(habit_goal[i]):
                    progress_labels[i-1].configure(text="Completed!")
                    habit_completed[i] = True
            show_habit(i)


# Function for edit button
def edit_habit(habit_id):
    while True:
        dialog_name = custom.CTkInputDialog(text="Please enter the name of the habit: ")
        dialog_name.geometry('325x175+800+500')
        dialog_name.title("Edit Habit")
        placehold_name = dialog_name.get_input()
        if placehold_name == "" or placehold_name == None:
            break
        elif len(placehold_name) > 15:
            messagebox.showerror("Error", "Please enter a name shorter than 15 characters.")
        else:
            habit_name[habit_id] = placehold_name
            break
    
    while True:
        dialog_goal = custom.CTkInputDialog(text="How many times do you aim to complete this habit per week? ")
        dialog_goal.geometry('325x175+825+500')
        dialog_goal.title("Edit Goal")
        placehold_goal = dialog_goal.get_input()
        if placehold_goal == None:
            dialog_goal.destroy
            break
        elif placehold_goal == "":
            messagebox.showerror("Error", "Please enter a number.")
        elif placehold_goal == "0":
            messagebox.showerror("Error", "Please enter a number greater than 0.")
        elif placehold_goal.isnumeric() == False:
            messagebox.showerror("Error", "Please enter a number.")
        elif int(placehold_goal) > 20:
            messagebox.showerror("Error", "Please enter a number less than 20.")
        else:
            habit_goal[habit_id] = placehold_goal
            break
    
    habit_progress[habit_id] = 0
    update_habit(habit_id)


# Function for create habit button
def create_habit():
    habit_id = find_lowest_available_habit_id()
    if habit_id == None:
        return
    
    create_habit = custom.CTkToplevel(app)
    create_habit.title("Create Habit")
    create_habit.geometry('400x500+750+280')
    create_habit.resizable(False, False)
    create_habit.attributes('-topmost', True)

    create_habit_label = custom.CTkLabel(create_habit,
                                text="Create Habit",
                                text_color="White",
                                font = ("",30))
    create_habit_label.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

    name_label = custom.CTkLabel(create_habit,
                                text="What is the name of the habit?",
                                text_color="White")
    name_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    name_input = custom.CTkEntry(create_habit,
                                placeholder_text = "Habit Name",
                                width = 200)
    name_input.place(relx=0.5, rely=0.31, anchor=tk.CENTER)

    goal_label = custom.CTkLabel(create_habit,
                                text="How many times do you want to complete it per week?",
                                text_color="White")
    goal_label.place(relx=0.5, rely=0.42, anchor=tk.CENTER)
    
    goal_options = custom.CTkOptionMenu(create_habit,
                                values=["1", "2", "3", "4", "5", "6", "7"],
                                width = 55)
    goal_options.place(relx=0.5, rely=0.48, anchor=tk.CENTER)

    category_label = custom.CTkLabel(create_habit,
                                text="What category is this habit?",
                                text_color="White")
    category_label.place(relx=0.5, rely=0.59, anchor=tk.CENTER)

    category_options = custom.CTkOptionMenu(create_habit,
                                values=["Health", "Fitness", "Learning", "Finance", "Fun", "Other"],
                                width = 55)
    category_options.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    def inside_create(habit_id):
        placehold_name = name_input.get()
        placehold_goal = goal_options.get()
        placehold_category = category_options.get()
        
        while True:
            if placehold_name == "":
                messagebox.showerror("Error", "Please enter a name with at least 1 character.", parent = create_habit)
                break
            elif len(placehold_name) > 15:
                messagebox.showerror("Error", "Please enter a name shorter than 15 characters.", parent = create_habit)
                break
            else:
                habit_name[habit_id] = str(placehold_name)
                habit_goal[habit_id] = int(placehold_goal)
                habit_category[habit_id] = str(placehold_category)
                habit_progress[habit_id] = 0
                habit_displayed[habit_id] = True
                update_habit(habit_id)
                show_habit(habit_id)
                create_habit.destroy()
                break
        
    def cancel_habit_button():
        create_habit.destroy()

    habit_create = custom.CTkButton(create_habit, text="Create",
                            text_color="Black",
                            width = 80,
                            command = lambda habit_id=habit_id: inside_create(habit_id))
    habit_create.place(relx=0.65, rely=0.9, anchor=tk.CENTER)

    habit_cancel = custom.CTkButton(create_habit, text="Cancel",
                            text_color="Black",
                            fg_color="Firebrick",
                            hover_color = "Orangered",
                            width = 80,
                            command=cancel_habit_button)
    habit_cancel.place(relx=0.35, rely=0.9, anchor=tk.CENTER)


# Buttons
create_habit_button = custom.CTkButton(master=app,
                            text="Create\n Habit",
                            text_color="Black",
                            width=70,
                            height=70,
                            command = create_habit)
create_habit_button.place(relx=0.9, rely=0.92, anchor=tk.CENTER)

instructions_button = custom.CTkButton(master=app,
                            text="Instructions",
                            text_color="Black")
instructions_button.place(relx=0.12, rely=0.8, anchor=tk.CENTER)

settings_button = custom.CTkButton(master=app,
                            text="Settings",
                            text_color="Black",
                            command = settings_button)
settings_button.place(relx=0.12, rely=0.875, anchor=tk.CENTER)

exit_button = custom.CTkButton(master=app,
                            text="Exit",
                            text_color="White",
                            fg_color = "Firebrick",
                            hover_color = "black",
                            command=exit_button)
exit_button.place(relx=0.12, rely=0.95, anchor=tk.CENTER)

reset_button = custom.CTkButton(master=app,
                            text="Reset",
                            text_color="White",
                            fg_color = "Firebrick",
                            border_color = "White",
                            border_width = 2,
                            width=70,
                            height=70,
                            command = reset_button)
reset_button.place(relx=0.75, rely=0.92, anchor=tk.CENTER)


# Habits
edit_icon = custom.CTkImage(light_image=Image.open("Edit Icon.png"), size = (15, 15))
delete_icon = custom.CTkImage(light_image=Image.open("Delete Icon.png"), size = (15, 15))
category = frame

for i in range(1,9):
    if i <= 4:
        habit_frame = custom.CTkFrame(app, width=150, height=200, border_color = category, border_width = 2)
        habit_frame.grid(row=1, column=i, padx=7, pady=(20,10), sticky="nsew")
        habit_frame.grid_propagate(False)
        habit_frames.append(habit_frame)
    else:
        habit_frame = custom.CTkFrame(app, width=150, height=200)
        habit_frame.grid(row=2, column=i-4, padx=7, pady=10, sticky="nsew")
        habit_frame.grid_propagate(False)
        habit_frames.append(habit_frame)    

    name_label = custom.CTkButton(habit_frame, 
                            width=120,
                            height=28,
                            text=str(habit_name[(i)]),
                            text_color="White",
                            border_color = "White",
                            border_width = 2,
                            fg_color = (frame),
                            corner_radius=7)
    name_labels.append(name_label)
    
    goal_label = custom.CTkButton(habit_frame,
                            width=100,
                            height=28,
                            text = "Goal: " + str(habit_goal[(i)]) + "/w",
                            text_color="White",
                            border_color = "White",
                            border_width = 2,
                            fg_color = (frame),
                            corner_radius=7)
    goal_labels.append(goal_label)

    progress_label = custom.CTkButton(habit_frame,
                            width=100,
                            height=28,
                            text="Progress: " + str(habit_progress[(i)]) + "%",
                            text_color="White",
                            border_color = "White",
                            border_width = 2,
                            fg_color = (frame),
                            corner_radius=7)
    progress_labels.append(progress_label)

    progress_bar = custom.CTkProgressBar(habit_frame, 
                            orientation="horizontal",
                            width = 100,
                            height = 15,
                            progress_color = "white")
    progress_bar.set(0)
    progress_bars.append(progress_bar)
    
    check_var = custom.StringVar(value=habit_checkbox[i])
    check_vars.append(check_var)

    complete_habit_button = custom.CTkCheckBox(habit_frame,
                            text = "", 
                            width = 26,
                            height = 26,
                            checkbox_width = 26,
                            checkbox_height = 26,
                            border_color = "white", 
                            command = lambda i=i: update_progress(i),
                            variable=check_var, 
                            onvalue="True", 
                            offvalue="False")
    complete_habit_buttons.append(complete_habit_button)

    edit_habit_button = custom.CTkButton(habit_frame,
                            image = edit_icon,
                            text="",
                            width=25,
                            height=25,
                            fg_color="White",
                            hover_color="LightGrey",
                            command = lambda i=i: edit_habit(i))
    edit_habit_buttons.append(edit_habit_button)
    
    delete_habit_button = custom.CTkButton(habit_frame,
                            image = delete_icon,
                            text = '',
                            width = 25,
                            height = 25,
                            fg_color = "Firebrick",
                            hover_color = "Orangered",
                            command = lambda i=i: delete_button(i))
    delete_habit_buttons.append(delete_habit_button)


# Calendar frames
invisible_frame = custom.CTkFrame(app, width=0, height=60)
invisible_frame.grid(row = 0, column = 0, pady = 10)

calendar_frames = []
calendar_checks = []
day_labels = []
date_labels = []

dates = []
for i in range (10):
    today = date.today()
    day = today - timedelta(days = i)
    dates.append(day.day)


days = []
for i in range (10):
    today = date.today()
    day = today - timedelta(days = i)
    days.append(day.strftime("%a").upper())


for i in range(10):
    if i == 9:
        width = 2
    else:
        width = 0

    if len(str(dates[(9-i)])) == 1:
        xpos = 0.42
    else:
        xpos = 0.35

    if str(days[9-i]) == "FRI":
        xpos2 = 0.35
    else:
        xpos2 = 0.3

    calendar_frame = custom.CTkFrame(app, width=55, height=70, border_color = gold, border_width = width)
    calendar_frame.place(relx = (0.013 + i*0.099), rely = 0.015)
    calendar_frame.grid_propagate(False)
    calendar_frames.append(calendar_frame)

    invisible_top_frame = custom.CTkFrame(calendar_frame, width=0, height=0)
    invisible_top_frame.grid(row = 0, column = 0, pady = 19)

    date_label = custom.CTkLabel(calendar_frame, text = dates[(9-i)], text_color = "white", font = ("Microsoft Sans Serif",13), height = 4)
    date_label.place(relx = xpos, rely = 0.08)
    date_labels.append(date_label)

    day_label = custom.CTkLabel(calendar_frame, text = days[(9-i)], text_color = "grey", font = ("Microsoft Sans Serif",10), height = 4)
    day_label.place(relx = xpos2, rely = 0.32)
    day_labels.append(day_label)

    for i in range(1,9):
        invisible_side_frame = custom.CTkFrame(calendar_frame, width=0, height=0, fg_color = frame)
        invisible_side_frame.grid(row = 0, column = 0, padx = 1.5)
        if i <= 4:
            calendar_check = custom.CTkButton(calendar_frame,
                                text="",
                                width=8,
                                height=8,
                                fg_color="red",
                                hover = False,
                                corner_radius = 3)
            calendar_check.grid(row=2, column=i, padx=2, pady=2)
            calendar_checks.append(calendar_check)
        else:
            calendar_check = custom.CTkButton(calendar_frame,
                                text="",
                                width=8,
                                height=8,
                                fg_color="red",
                                hover = False,
                                corner_radius = 3)
            calendar_check.grid(row=3, column=i-4, padx=2, pady=2)
            calendar_checks.append(calendar_check)


initial_open()

app.mainloop()