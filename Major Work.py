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
custom.set_appearance_mode("Dark") # Sets the customtkinter appearance theme to dark mode
current_theme = custom.get_appearance_mode()
custom.set_default_color_theme("blue")  # Sets the customtkinter colour theme to blue


# Reads the habits.csv file to receive all the saved data of each habit
def read_csv(): 
    global hdf, cdf
    hdf = pd.read_csv("Habits.csv")
    cdf = pd.read_csv("Calendar.csv")
read_csv() # Immediately reads the csv file upon opening the program


# Writes the data onto the habits.csv and calendar.csv files to save any changes
def write_csv(habit_id):
    hdf.iloc[(habit_id - 1),0] = habit_name[habit_id]
    hdf.iloc[(habit_id - 1),1] = habit_goal[habit_id]
    hdf.iloc[(habit_id - 1),2] = habit_progress[habit_id]
    hdf.iloc[(habit_id - 1),3] = habit_completed[habit_id]
    hdf.iloc[(habit_id - 1),4] = habit_displayed[habit_id]
    hdf.iloc[(habit_id - 1),5] = habit_checkbox[habit_id]
    hdf.iloc[(habit_id - 1),6] = habit_category[habit_id]
    cdf.iloc[0,(habit_id - 1)] = habit_category[habit_id] # Updates the categories for today
    
    hdf.to_csv('Habits.csv', index = False) # Writes the new data to the csv files
    cdf.to_csv('Calendar.csv', index = False)


# Initialises habit variables so they all are defined and have an initial value
habit_name =      {1: hdf.iloc[0,0], 2: hdf.iloc[1,0], 3: hdf.iloc[2,0], 4: hdf.iloc[3,0], 5: hdf.iloc[4,0], 6: hdf.iloc[5,0], 7: hdf.iloc[6,0], 8: hdf.iloc[7,0]}
habit_goal =      {1: hdf.iloc[0,1], 2: hdf.iloc[1,1], 3: hdf.iloc[2,1], 4: hdf.iloc[3,1], 5: hdf.iloc[4,1], 6: hdf.iloc[5,1], 7: hdf.iloc[6,1], 8: hdf.iloc[7,1]}
habit_progress =  {1: hdf.iloc[0,2], 2: hdf.iloc[1,2], 3: hdf.iloc[2,2], 4: hdf.iloc[3,2], 5: hdf.iloc[4,2], 6: hdf.iloc[5,2], 7: hdf.iloc[6,2], 8: hdf.iloc[7,2]}
habit_completed = {1: hdf.iloc[0,3], 2: hdf.iloc[1,3], 3: hdf.iloc[2,3], 4: hdf.iloc[3,3], 5: hdf.iloc[4,3], 6: hdf.iloc[5,3], 7: hdf.iloc[6,3], 8: hdf.iloc[7,3]}
habit_displayed = {1: hdf.iloc[0,4], 2: hdf.iloc[1,4], 3: hdf.iloc[2,4], 4: hdf.iloc[3,4], 5: hdf.iloc[4,4], 6: hdf.iloc[5,4], 7: hdf.iloc[6,4], 8: hdf.iloc[7,4]}
habit_checkbox =  {1: hdf.iloc[0,5], 2: hdf.iloc[1,5], 3: hdf.iloc[2,5], 4: hdf.iloc[3,5], 5: hdf.iloc[4,5], 6: hdf.iloc[5,5], 7: hdf.iloc[6,5], 8: hdf.iloc[7,5]}
habit_category =  {1: hdf.iloc[0,6], 2: hdf.iloc[1,6], 3: hdf.iloc[2,6], 4: hdf.iloc[3,6], 5: hdf.iloc[4,6], 6: hdf.iloc[5,6], 7: hdf.iloc[6,6], 8: hdf.iloc[7,6]}
appearance_label = None
created = False
background = "#242424"
frame = "#2b2b2b"
gold = "#daa520"

# List of all the calendar days and their data from the calendar csv
calendar_days = []
day0 = {1: cdf.iloc[0,0], 2: cdf.iloc[0,1], 3: cdf.iloc[0,2], 4: cdf.iloc[0,3], 5: cdf.iloc[0,4], 6: cdf.iloc[0,5], 7: cdf.iloc[0,6], 8: cdf.iloc[0,7]}   
day1 = {1: cdf.iloc[1,0], 2: cdf.iloc[1,1], 3: cdf.iloc[1,2], 4: cdf.iloc[1,3], 5: cdf.iloc[1,4], 6: cdf.iloc[1,5], 7: cdf.iloc[1,6], 8: cdf.iloc[1,7]}
day2 = {1: cdf.iloc[2,0], 2: cdf.iloc[2,1], 3: cdf.iloc[2,2], 4: cdf.iloc[2,3], 5: cdf.iloc[2,4], 6: cdf.iloc[2,5], 7: cdf.iloc[2,6], 8: cdf.iloc[2,7]}
day3 = {1: cdf.iloc[3,0], 2: cdf.iloc[3,1], 3: cdf.iloc[3,2], 4: cdf.iloc[3,3], 5: cdf.iloc[3,4], 6: cdf.iloc[3,5], 7: cdf.iloc[3,6], 8: cdf.iloc[3,7]}
day4 = {1: cdf.iloc[4,0], 2: cdf.iloc[4,1], 3: cdf.iloc[4,2], 4: cdf.iloc[4,3], 5: cdf.iloc[4,4], 6: cdf.iloc[4,5], 7: cdf.iloc[4,6], 8: cdf.iloc[4,7]}
day5 = {1: cdf.iloc[5,0], 2: cdf.iloc[5,1], 3: cdf.iloc[5,2], 4: cdf.iloc[5,3], 5: cdf.iloc[5,4], 6: cdf.iloc[5,5], 7: cdf.iloc[5,6], 8: cdf.iloc[5,7]}
day6 = {1: cdf.iloc[6,0], 2: cdf.iloc[6,1], 3: cdf.iloc[6,2], 4: cdf.iloc[6,3], 5: cdf.iloc[6,4], 6: cdf.iloc[6,5], 7: cdf.iloc[6,6], 8: cdf.iloc[6,7]}
day7 = {1: cdf.iloc[7,0], 2: cdf.iloc[7,1], 3: cdf.iloc[7,2], 4: cdf.iloc[7,3], 5: cdf.iloc[7,4], 6: cdf.iloc[7,5], 7: cdf.iloc[7,6], 8: cdf.iloc[7,7]}
day8 = {1: cdf.iloc[8,0], 2: cdf.iloc[8,1], 3: cdf.iloc[8,2], 4: cdf.iloc[8,3], 5: cdf.iloc[8,4], 6: cdf.iloc[8,5], 7: cdf.iloc[8,6], 8: cdf.iloc[8,7]}
day9 = {1: cdf.iloc[9,0], 2: cdf.iloc[9,1], 3: cdf.iloc[9,2], 4: cdf.iloc[9,3], 5: cdf.iloc[9,4], 6: cdf.iloc[9,5], 7: cdf.iloc[9,6], 8: cdf.iloc[9,7]}
calendar_days.extend([day0,day1,day2,day3,day4,day5,day6,day7,day8,day9])


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

# Shuffles the days down and their data as the days change
def shuffle_days():
    today = date.today() # Finds todays date
    if today.day > int(cdf.iloc[0,8]):
        difference = (today.day) - int(cdf.iloc[0,8]) # Finds the difference between today's date and the date of the most recent entry
    else:
        difference = (today.day) + 30 - int(cdf.iloc[0,8]) # Handles the case where the date today is in the next month from the last entry

    if difference >= 10: # Checks if the difference is greater than 10 and then just sets it to 9 so that it only shuffles down the necessary amount
        difference = 10

    for i in range(9, difference - 1, -1): # AI used here as it was a complicated operation with no online solutions
        calendar_days[i] = calendar_days[i - difference] # Shuffles the days down by the difference
    
    for i in range(difference): # Sets the days between the last entry and today to all False (makes them empty)
        calendar_days[i] = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False}
    
    for i in range(10):
        for j in range(8):
            cdf.iloc[i, j] = (calendar_days[i])[j + 1] # AI used here as I couldn't figure out how to set all the data base values to each of the calendar days values

    for i in range (10): # Sets all the new dates for each day
        today = date.today()
        day = today - timedelta(days = i)
        cdf.iloc[i, 8] = day.day

    if difference != 0:
        for i in range(8):
            habit_checkbox[i+1] = False
            if complete_habit_buttons[i].get() == True: # If the habit checkbox is true toggle it to false
                complete_habit_buttons[i].toggle()
            hdf.iloc[(i),5] = habit_checkbox[i+1]
        hdf.to_csv('Habits.csv', index = False)
        cdf.to_csv('Calendar.csv', index = False)
        
# Assigns a colour to each category
def category_colour(habit_id):
    if habit_category[habit_id] == "Health":
        return "#ffb3ba"
    elif habit_category[habit_id] == "Fitness":
        return "#baffc9"
    elif habit_category[habit_id] == "Learning":
        return "#bae1ff"
    elif habit_category[habit_id] == "Finance":
        return "#ffffba"
    elif habit_category[habit_id] == "Fun":
        return "#ffdfba"
    elif habit_category[habit_id] == "Other":
        return "#eecbff"
    else:
        return ""


# Function to find the lowest available habit id
def find_lowest_available_habit_id(): 
    lowest_id = None
    for habit_id, display_status in habit_displayed.items(): # AI used here as it was a complicated function that I couldn't find an online solution to
        if display_status == False:  # Checks if habit slot is available
            if lowest_id is None or habit_id < lowest_id:
                lowest_id = habit_id
                return lowest_id # Returns the lowest available habit slot ID
    if lowest_id == None: # Shows an error box if no lowest id is found (maximum habits)
        messagebox.showerror("Error", "You have reached the maximum amount of habits.")
        return lowest_id


# Function for exit button
def exit_button():
    exit_confirm = custom.CTkToplevel(app) # Creates exit confirm window
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
    global edit
    reset_confirm = custom.CTkToplevel(app) # Creates reset confirm window
    reset_confirm.title("Reset Confirmation")
    reset_confirm.geometry('250x120+900+500')
    reset_confirm.resizable(False, False)
    reset_confirm.attributes('-topmost', True)
    
    def reset_habits():
        global edit
        for i in range(1,9): # Turns all the habit elements invisible
            name_labels[i-1].grid_forget()
            goal_labels[i-1].grid_forget()
            progress_labels[i-1].grid_forget()
            progress_bars[i-1].grid_forget()
            complete_habit_buttons[i-1].grid_forget()
            edit_habit_buttons[i-1].grid_forget()
            delete_habit_buttons[i-1].grid_forget()
            habit_name[i] = "Habit " + str(i) # Resets all the habit data to defaults
            habit_goal[i] = 0
            habit_progress[i] = 0
            habit_displayed[i] = False # Sets habit slot to available
            habit_completed[i] = False
            habit_checkbox[i] = False
            habit_category[i] = False
            check_value = complete_habit_buttons[i-1].get() # If the checkbox is on it is toggled off
            if check_value == "True":
                complete_habit_buttons[i-1].toggle()
            edit = False
            update_habit(i)
            write_csv(i)
        reset_confirm.destroy()

    reset_label = custom.CTkLabel(master=reset_confirm,
                            text="Are you sure you want to reset?")
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
    global edit
    name_labels[habit_id-1].grid_forget() # Sets all of the habit elements to invisible
    goal_labels[habit_id-1].grid_forget()
    progress_labels[habit_id-1].grid_forget()
    progress_bars[habit_id-1].grid_forget()
    complete_habit_buttons[habit_id-1].grid_forget()
    edit_habit_buttons[habit_id-1].grid_forget()
    delete_habit_buttons[habit_id-1].grid_forget()
    habit_name[habit_id] = "Habit " + str(habit_id) # Sets all of the habit data to defaults
    habit_goal[habit_id] = 0
    habit_progress[habit_id] = 0
    habit_displayed[habit_id] = False # Sets habit slot to available
    habit_completed[habit_id] = False
    habit_checkbox[habit_id] = False
    habit_category[habit_id] = False
    check_value = complete_habit_buttons[habit_id-1].get()
    if check_value == "True": # If the habit checkbox is true set it to false
        complete_habit_buttons[habit_id-1].toggle()
    edit = False
    update_habit(habit_id)
    write_csv(habit_id)
    

# Clear the calendar history (removes all indicators)
def clear_history():
    global edit
    clear_confirm = custom.CTkToplevel(app) # Creates clear confirm window
    clear_confirm.title("Clear Confirmation")
    clear_confirm.geometry('250x120+900+500')
    clear_confirm.resizable(False, False)
    clear_confirm.attributes('-topmost', True)
    
    def clear_calendar():
        for i in range(72):
            calendar_checks[i].configure(fg_color = "transparent") # Changes all the calendar indicators to transparent

        for i in range(1,10):
            for j in range(8):
                cdf.iloc[i, j] = False # Sets all of the calendar csv to false except today

        cdf.to_csv('Calendar.csv', index = False)
        clear_confirm.destroy()

    clear_label = custom.CTkLabel(master=clear_confirm,
                            text="Are you sure you want to\n clear your calendar history?")
    clear_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    yes_button = custom.CTkButton(master=clear_confirm,
                            text="Yes",
                            text_color="Black",
                            fg_color="Firebrick",
                            hover_color = "Orangered",
                            width = 80,
                            command=clear_calendar)
    yes_button.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

    no_button = custom.CTkButton(master=clear_confirm,
                            text="No",
                            text_color="Black",
                            width = 80,
                            command=clear_confirm.destroy)
    no_button.place(relx=0.3, rely=0.7, anchor=tk.CENTER)


# Function for changing appearance
def change_appearance(mode:str):
    global appearance_menu, current_theme
    current_theme = mode
    custom.set_appearance_mode(mode) # Changes the appearance mode to the selected theme

    if current_theme == "Light":
        colour_variable = "Black"
    else:
        colour_variable = "White"

    for i in range(8): # Changes the text colours to be high contrasting to the background colour
        name_labels[i].configure(text_color=colour_variable, border_color=colour_variable)
        goal_labels[i].configure(text_color=colour_variable, border_color=colour_variable)
        progress_labels[i].configure(text_color=colour_variable, border_color=colour_variable)
    

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


# Function for instructions button
def instructions():
    instructions_window = custom.CTkToplevel(app) # Creates the instructions window
    instructions_window.title("Instructions")
    instructions_window.geometry('600x600+700+200')
    instructions_window.resizable(False, False)
    instructions_window.attributes('-topmost', True)
    app.withdraw() # Makes the main window disappear

    title_label = custom.CTkLabel(master=instructions_window,
                                  text = "Welcome to the Habit Tracker!",
                                  font = ("", 20))
    title_label.place(relx = 0.28, rely = 0.08)

    instructions_label = custom.CTkLabel(master=instructions_window,
                                        text="Here are the instructions on how to use it:\n\n"
                                             "1. To create a new habit, click on the 'Create Habit' button.\n\n"
                                             "2. Fill in the habit name then select a goal and category.\n\n"
                                             "3. Once created, the habit will appear on the main window.\n\n"
                                             "4. To edit a habit, click on the 'Edit' button at the bottom of the habit.\n\n"
                                             "5. To delete a habit, click on the 'Delete' button at the bottom of the habit.\n\n"
                                             "6. To mark a habit as completed, check the checkbox at the bottom of the habit.\n\n"
                                             "7. To clear the history of completed habits, click on the 'Clear History' button.\n\n"
                                             "8. To exit the app, click on the 'Exit' button.\n\n"
                                             "That's it! Enjoy tracking your habits and stay motivated!")
    instructions_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    close_button = custom.CTkButton(master=instructions_window,
                                    text="Close",
                                    text_color="Black",
                                    width=80,
                                    command = lambda: [app.deiconify(), instructions_window.destroy()])
    close_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    

# Function for updating habit progress
def update_progress(habit_id):
    checkbox = check_vars[habit_id-1].get()
    if checkbox == 'True': # Checks if the checkbox is on
        if (habit_progress[habit_id]) < int(habit_goal[habit_id]):
            habit_progress[habit_id] += 1
            habit_percentage = (habit_progress[habit_id]/int(habit_goal[habit_id])) # Calculates the habit percentage
            progress_labels[habit_id-1].configure(text="Progress: " + (f"{(habit_percentage):.0%}")) # Displays the percentage
            progress_bars[habit_id-1].set(habit_percentage)
            if habit_progress[habit_id] >= int(habit_goal[habit_id]): # Checks if the habit has been completed
                progress_labels[habit_id-1].configure(text="Completed!")
                habit_completed[habit_id] = True
        habit_checkbox[habit_id] = True
        today_checks[habit_id-1].configure(fg_color = category_colour(habit_id)) # Turns on the associated calendar indicator
    if checkbox == 'False': # Checks if the checkbox is off
        if habit_progress[habit_id] > 0: 
            habit_progress[habit_id] -= 1
            habit_percentage = (habit_progress[habit_id]/int(habit_goal[habit_id])) # Calculates the habit percentage
            progress_labels[habit_id-1].configure(text="Progress: " + (f"{(habit_percentage):.0%}")) # Displays the habit percentage
            progress_bars[habit_id-1].set(habit_percentage)
            if habit_progress[habit_id] < int(habit_goal[habit_id]):
                progress_labels[habit_id-1].configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
                habit_completed[habit_id] = False
        habit_checkbox[habit_id] = False
        today_checks[habit_id-1].configure(fg_color = "") # Sets today's indicator to invisible
    write_csv(habit_id)


# Updates habit buttons and labels
def update_habit(habit_id):
    global edit
    name_labels[habit_id-1].configure(text= str(habit_name[habit_id])) # Displays the current habit name
    goal_labels[habit_id-1].configure(text="Goal: " + str(habit_goal[habit_id]) + "/w") # Displays the current goal
    if habit_progress[habit_id] == 0 and habit_goal[habit_id] == 0:
        habit_percentage = 0
    else:
        habit_percentage = (habit_progress[habit_id]/int(habit_goal[habit_id]))
    progress_labels[habit_id-1].configure(text="Progress: " + (f"{(habit_percentage):.0%}")) # Displays the progress
    progress_bars[habit_id-1].set(habit_percentage)
    habit_frames[habit_id-1].configure(border_color = category_colour(habit_id))
    if edit == True:
        pass
    else:
        today_checks[habit_id-1].configure(fg_color = category_colour(habit_id)) # Turns on today's indicator
    edit = False
    write_csv(habit_id)


# Function for showing a new habit
def show_habit(habit_id): # Places all of the habit elements
    name_labels[habit_id-1].grid(row=0, column=0, padx=15, pady=(18, 5), sticky = "we")
    goal_labels[habit_id-1].grid(row=1, column=0, padx=15, pady=5,  sticky = "we")
    progress_labels[habit_id-1].grid(row=2, column=0, padx=15, pady=5,  sticky = "we")
    progress_bars[habit_id-1].grid(row=3, column=0, padx=15, pady=5,  sticky = "we")
    complete_habit_buttons[habit_id-1].grid(row=4, column=0, padx=(5,10), pady=5, sticky = "e")
    edit_habit_buttons[habit_id-1].grid(row=4, column=0, padx=(5,5), pady=5)
    delete_habit_buttons[habit_id-1].grid(row=4, column=0, padx=(15,0), pady=5, sticky = "w")


# Initially displays all the habits that were previously open
def initial_open():
    for i in range(1,9): # Goes through all the habits and displays their progresses
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
    global edit
    edit_habit = custom.CTkToplevel(app) # Creates the edit window
    edit_habit.title("Edit Habit")
    edit_habit.geometry('400x500+750+280')
    edit_habit.resizable(False, False)
    edit_habit.attributes('-topmost', True)

    edit_habit_label = custom.CTkLabel(edit_habit,
                                text="Edit Habit",
                                font = ("",30))
    edit_habit_label.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

    name_label = custom.CTkLabel(edit_habit,
                                text="What is the name of the habit?")
    name_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    name_input = custom.CTkEntry(edit_habit,
                                placeholder_text = habit_name[habit_id],
                                width = 200)
    name_input.place(relx=0.5, rely=0.31, anchor=tk.CENTER)

    goal_label = custom.CTkLabel(edit_habit,
                                text="How many times do you want to complete it per week?")
    goal_label.place(relx=0.5, rely=0.42, anchor=tk.CENTER)
    
    goal_options = custom.CTkOptionMenu(edit_habit,
                                values=["1", "2", "3", "4", "5", "6", "7"],
                                width = 55)
    goal_options.place(relx=0.5, rely=0.48, anchor=tk.CENTER)
    goal_options.set(str(habit_goal[habit_id]))

    category_label = custom.CTkLabel(edit_habit,
                                text="What category is this habit?")
    category_label.place(relx=0.5, rely=0.59, anchor=tk.CENTER)

    category_options = custom.CTkOptionMenu(edit_habit,
                                values=["Health", "Fitness", "Learning", "Finance", "Fun", "Other"],
                                width = 55)
    category_options.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    category_options.set(str(habit_category[habit_id]))

    '''This function receives the information from the edit input fields and checks for errors before updating
    the associated habit data. The function is broken into three if main if statements for if the goal was changed,
    or category was changed.'''
    def save_edit(habit_id):
        global edit
        placehold_name = name_input.get() # Gets the input from the name, goal and category fields
        placehold_goal = goal_options.get()
        placehold_category = category_options.get()
        
        if placehold_name != "": # If the habit name was changed
            while True: # Checks for user errors
                if placehold_name == "":
                    messagebox.showerror("Error", "Please enter a name with at least 1 character.", parent = edit_habit)
                    break
                elif len(placehold_name) > 14:
                    messagebox.showerror("Error", "Please enter a name shorter than 14 characters.", parent = edit_habit)
                    break
                elif placehold_name == "null":
                    messagebox.showerror("Error", "You can't enter 'null' as a name.", parent = edit_habit)
                    break
                else:
                    habit_name[habit_id] = str(placehold_name)
                    habit_displayed[habit_id] = True
                    edit = True
                    edit_habit.destroy()
                    break
                
        if str(placehold_category) != str(habit_category[habit_id]): # If the category was changed
            habit_category[habit_id] = str(placehold_category)
            habit_displayed[habit_id] = True
            edit = False
            update_habit(habit_id)
            show_habit(habit_id)
            if placehold_name == "":
                edit_habit.destroy()

        if int(placehold_goal) != int(habit_goal[habit_id]): # If the goal was changed
            check_value = complete_habit_buttons[habit_id-1].get()
            if check_value == "True":
                complete_habit_buttons[habit_id-1].toggle()
            habit_goal[habit_id] = int(placehold_goal)
            habit_progress[habit_id] = 0
            edit = True
            habit_completed[habit_id] = False
            habit_checkbox[habit_id] = False
            if placehold_name == "":
                edit_habit.destroy()
        else:
            edit = False

        habit_category[habit_id] = str(placehold_category)
        update_habit(habit_id)
        show_habit(habit_id)
                

    def cancel_edit_button():
        edit_habit.destroy()

    habit_save = custom.CTkButton(edit_habit, text="Save",
                            text_color="Black",
                            width = 80,
                            command = lambda habit_id=habit_id: save_edit(habit_id))
    habit_save.place(relx=0.65, rely=0.9, anchor=tk.CENTER)

    habit_cancel = custom.CTkButton(edit_habit, text="Cancel",
                            text_color="Black",
                            fg_color="Firebrick",
                            hover_color = "Orangered",
                            width = 80,
                            command=cancel_edit_button)
    habit_cancel.place(relx=0.35, rely=0.9, anchor=tk.CENTER)


# Function for create habit button
def create_habit():
    global edit
    habit_id = find_lowest_available_habit_id()
    if habit_id == None:
        return
    
    create_habit = custom.CTkToplevel(app) # Creates the habit window
    create_habit.title("Create Habit")
    create_habit.geometry('400x500+750+280')
    create_habit.resizable(False, False)
    create_habit.attributes('-topmost', True)

    create_habit_label = custom.CTkLabel(create_habit,
                                text="Create Habit",
                                font = ("",30))
    create_habit_label.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

    name_label = custom.CTkLabel(create_habit,
                                text="What is the name of the habit?")
    name_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    name_input = custom.CTkEntry(create_habit,
                                placeholder_text = "Habit Name",
                                width = 200)
    name_input.place(relx=0.5, rely=0.31, anchor=tk.CENTER)

    goal_label = custom.CTkLabel(create_habit,
                                text="How many times do you want to complete it per week?")
    goal_label.place(relx=0.5, rely=0.42, anchor=tk.CENTER)
    
    goal_options = custom.CTkOptionMenu(create_habit,
                                values=["1", "2", "3", "4", "5", "6", "7"],
                                width = 55)
    goal_options.place(relx=0.5, rely=0.48, anchor=tk.CENTER)

    category_label = custom.CTkLabel(create_habit,
                                text="What category is this habit?")
    category_label.place(relx=0.5, rely=0.59, anchor=tk.CENTER)

    category_options = custom.CTkOptionMenu(create_habit,
                                values=["Health", "Fitness", "Learning", "Finance", "Fun", "Other"],
                                width = 55)
    category_options.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    def inside_create(habit_id):
        global edit
        placehold_name = name_input.get() # Gets all the values from the input fields
        placehold_goal = goal_options.get()
        placehold_category = category_options.get()
        
        while True:
            if placehold_name == "": # If the name field is empty
                messagebox.showerror("Error", "Please enter a name with at least 1 character.", parent = create_habit)
                break
            elif len(placehold_name) > 14: # If the name field is too long
                messagebox.showerror("Error", "Please enter a name shorter than 14 characters.", parent = create_habit)
                break
            elif placehold_name == "null": # If the name field is null
                messagebox.showerror("Error", "You can't enter 'null' as a name.", parent = create_habit)
                break
            else:
                habit_name[habit_id] = str(placehold_name) # Sets the habit data to the entered inputs
                habit_goal[habit_id] = int(placehold_goal)
                habit_category[habit_id] = str(placehold_category)
                habit_progress[habit_id] = 0
                habit_displayed[habit_id] = True
                habit_completed[habit_id] = False
                habit_checkbox[habit_id] = False
                edit = True
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

clear_button = custom.CTkButton(master=app,
                            text="Clear\n History",
                            text_color="White",
                            fg_color = "Firebrick",
                            width=70,
                            height=70,
                            command = clear_history)
clear_button.place(relx=0.6, rely=0.92, anchor=tk.CENTER)

instructions_button = custom.CTkButton(master=app,
                            text="Instructions",
                            text_color="Black",
                            command=instructions)
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
                            width=70,
                            height=70,
                            command = reset_button)
reset_button.place(relx=0.75, rely=0.92, anchor=tk.CENTER)


# Habits
edit_icon = custom.CTkImage(light_image=Image.open("Images\Edit Icon.png"), size = (15, 15))
delete_icon = custom.CTkImage(light_image=Image.open("Images\Delete Icon.png"), size = (15, 15))
if current_theme == "Light":
    colour_variable = "Black"
else:
    colour_variable = "White"

for i in range(1,9): # Creates all the habit frames and elements
    category = category_colour(i)
    if i <= 4: # First row of frames
        habit_frame = custom.CTkFrame(app, width=150, height=200, border_color = category, border_width = 2)
        habit_frame.grid(row=1, column=i, padx=7, pady=(20,10), sticky="nsew")
        habit_frame.grid_propagate(False)
        habit_frames.append(habit_frame)
    else: # Second row of frames
        habit_frame = custom.CTkFrame(app, width=150, height=200, border_color = category, border_width = 2)
        habit_frame.grid(row=2, column=i-4, padx=7, pady=10, sticky="nsew")
        habit_frame.grid_propagate(False)
        habit_frames.append(habit_frame)    

    name_label = custom.CTkButton(habit_frame, 
                            width=120,
                            height=28,
                            text=str(habit_name[(i)]),
                            text_color=colour_variable,
                            border_color = "White",
                            fg_color= "transparent",
                            font = ("", 10),
                            border_width = 2,
                            corner_radius=7,
                            hover = False)
    name_labels.append(name_label)
    
    goal_label = custom.CTkButton(habit_frame,
                            width=100,
                            height=28,
                            text = "Goal: " + str(habit_goal[(i)]) + "/w",
                            border_color = "White",
                            fg_color= "transparent",
                            border_width = 2,
                            corner_radius=7,
                            hover = False)
    goal_labels.append(goal_label)

    progress_label = custom.CTkButton(habit_frame,
                            width=100,
                            height=28,
                            text="Progress: " + str(habit_progress[(i)]) + "%",
                            border_color = "White",
                            fg_color= "transparent",
                            border_width = 2,
                            corner_radius=7,
                            hover = False)
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

today_checks = []
calendar_frames = []
calendar_checks = []
day_labels = []
date_labels = []

dates = []
for i in range(10): # Calculates the dates of the last 10 days
    today = date.today()
    day = today - timedelta(days = i)
    dates.append(day.day)

days = []
for i in range(10):
    today = date.today()
    day = today - timedelta(days = i)
    days.append(day.strftime("%a").upper()) # Gets the day in all caps

for i in range(10): # Creates all of the calendar frames and elements 10 times
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

    date_label = custom.CTkLabel(calendar_frame, text = dates[(9-i)], font = ("Microsoft Sans Serif",13), height = 4)
    date_label.place(relx = xpos, rely = 0.08)
    date_labels.append(date_label)

    day_label = custom.CTkLabel(calendar_frame, text = days[(9-i)], text_color = "grey", font = ("Microsoft Sans Serif",10), height = 4)
    day_label.place(relx = xpos2, rely = 0.32)
    day_labels.append(day_label)

    if i == 9: # Creates todays calendar indicators
        for j in range(1,9):
            if habit_checkbox[j] == True and (calendar_days[0])[j] == habit_category[j]:
                category = category_colour(j)
            else:
                category = ""

            invisible_side_frame = custom.CTkFrame(calendar_frame, width=0, height=0, fg_color = frame)
            invisible_side_frame.grid(row = 0, column = 0, padx = 1.5)
            if j <= 4:
                today_check = custom.CTkButton(calendar_frame,
                                    text="",
                                    width=8,
                                    height=8,
                                    fg_color=category,
                                    hover = False,
                                    corner_radius = 3)
                today_check.grid(row=2, column=j, padx=2, pady=2)
                today_checks.append(today_check)
            else:
                today_check = custom.CTkButton(calendar_frame,
                                    text="",
                                    width=8,
                                    height=8,
                                    fg_color=category,
                                    hover = False,
                                    corner_radius = 3)
                today_check.grid(row=3, column=j-4, padx=2, pady=2)
                today_checks.append(today_check)
    else: # Creates all of the other calendar indicators
        for j in range(1,9): # Identifies all the categories of the habits in the last 10 days and assigns them the right colour
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
                category = ""

            invisible_side_frame = custom.CTkFrame(calendar_frame, width=0, height=0, fg_color = frame) # Used to position the checks correctly
            invisible_side_frame.grid(row = 0, column = 0, padx = 1.5)
            if j <= 4: # First row of indicators
                calendar_check = custom.CTkButton(calendar_frame,
                                    text="",
                                    width=8,
                                    height=8,
                                    fg_color=category,
                                    hover = False,
                                    corner_radius = 3)
                calendar_check.grid(row=2, column=j, padx=2, pady=2)
                calendar_checks.append(calendar_check)
            else: # Second row of indicators
                calendar_check = custom.CTkButton(calendar_frame,
                                    text="",
                                    width=8,
                                    height=8,
                                    fg_color=category,
                                    hover = False,
                                    corner_radius = 3)
                calendar_check.grid(row=3, column=j-4, padx=2, pady=2)
                calendar_checks.append(calendar_check)


# Category list
category_frame = custom.CTkFrame(app, width=150, height=120, border_color = category, border_width = 2)
category_frame.place(relx = 0.26, rely = 0.8)

health_label = custom.CTkLabel(category_frame, text="Health", font=("", 10))
health_label.place(relx=0.18, rely=0.04)

health_category = custom.CTkButton(category_frame,
                                    text="",
                                    width=12,
                                    height=12,
                                    fg_color="#ffb3ba",
                                    hover = False,
                                    corner_radius = 3)
health_category.place(relx = 0.07, rely = 0.1)

learning_label = custom.CTkLabel(category_frame, text="Learning", font=("", 10))
learning_label.place(relx=0.18, rely=0.39)

learning_category = custom.CTkButton(category_frame,
                                    text="",
                                    width=12,
                                    height=12,
                                    fg_color="#bae1ff",
                                    hover = False,
                                    corner_radius = 3)
learning_category.place(relx = 0.07, rely = 0.45)

fitness_label = custom.CTkLabel(category_frame, text="Fitness", font=("", 10))
fitness_label.place(relx=0.18, rely=0.74)

fitness_category = custom.CTkButton(category_frame,
                                    text="",
                                    width=12,
                                    height=12,
                                    fg_color="#baffc9",
                                    hover = False,
                                    corner_radius = 3)
fitness_category.place(relx = 0.07, rely = 0.8)

finance_label = custom.CTkLabel(category_frame, text="Finance", font=("", 10), fg_color="transparent")
finance_label.place(relx=0.64, rely=0.04)

finance_category = custom.CTkButton(category_frame,
                                    text="",
                                    width=12,
                                    height=12,
                                    fg_color="#ffffba",
                                    hover = False,
                                    corner_radius = 3)
finance_category.place(relx = 0.53, rely = 0.1)

fun_label = custom.CTkLabel(category_frame, text="Fun", font=("", 10), fg_color="transparent")
fun_label.place(relx=0.64, rely=0.39)

fun_category = custom.CTkButton(category_frame,
                                    text="",
                                    width=12,
                                    height=12,
                                    fg_color="#ffdfba",
                                    hover = False,
                                    corner_radius = 3)
fun_category.place(relx = 0.53, rely = 0.45)

other_label = custom.CTkLabel(category_frame, text="Other", font=("", 10), fg_color="transparent")
other_label.place(relx=0.64, rely=0.74)

other_category = custom.CTkButton(category_frame,
                                    text="",
                                    width=12,
                                    height=12,
                                    fg_color="#eecbff",
                                    hover = False,
                                    corner_radius = 3)
other_category.place(relx = 0.53, rely = 0.8)

shuffle_days()
initial_open()

app.mainloop()