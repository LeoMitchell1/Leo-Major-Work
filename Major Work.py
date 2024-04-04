import customtkinter as custom
import tkinter as tk
from tkinter import *
from PIL import Image

# Go through and do Error management for all inputs
# Add a dialog window for exit confirmation
# Do the create habit dialog window
# Do the edit habit dialog window

# Creates main app window
app = custom.CTk()
app.title("Habit Tracker")
app.geometry('600x600')
app.resizable(False, False)
custom.set_appearance_mode("dark")
custom.set_default_color_theme("green")


# Initialises habit variables
habit_name = {1: "Habit 1", 2: "Habit 2"}
habit_goal = {1: 7, 2: 7}
habit_progress = {1: 0, 2: 0}
habit_completed = {1: False, 2: False}


# Function for exit button
def exit_button():
    exit()


# Function for updating habit progress
def update_progress(habit_id):
    global check_var
    checkbox = check_var.get()
    if checkbox == 'on':
        if habit_progress[habit_id] < habit_goal[habit_id]:
            habit_progress[habit_id] += 1
            habit_percentage = (habit_progress[habit_id]/habit_goal[habit_id])
            if habit_id == 1:  
                progress_label_1.configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
            elif habit_id == 2:
                progress_label_1.configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
            if habit_progress[habit_id] >= habit_goal[habit_id]:
                progress_label_1.configure(text="Habit Completed!")
                habit_completed[habit_id] = True


# Function for delete button
def delete(habit_id):
    if habit_id == 1:
        name_label_1.place_forget()
        goal_label_1.place_forget()
        progress_label_1.place_forget()
        complete_habit_button_1.place_forget()
        edit_habit_button_1.place_forget()
        delete_habit_button_1.place_forget()


# Function for showing a new habit
def show_habit(habit_id):
    if habit_id == 1:
        name_label_1.place(relx=0.14, rely=0.08, anchor=tk.CENTER)
        goal_label_1.place(relx=0.14, rely=0.14, anchor=tk.CENTER)
        progress_label_1.place(relx=0.14, rely=0.2, anchor=tk.CENTER)
        complete_habit_button_1.place(relx=0.21, rely=0.28, anchor=tk.CENTER)
        edit_habit_button_1.place(relx=0.145, rely=0.28, anchor=tk.CENTER)
        delete_habit_button_1.place(relx=0.08, rely=0.28, anchor=tk.CENTER)


def create_habit(habit_id):
    dialog_name = custom.CTkInputDialog(text="Please enter the name of the habit: ")
    habit_name[habit_id] = dialog_name.get_input()
    dialog_goal = custom.CTkInputDialog(text="How many times do you aim to complete this habit per week? ")
    habit_goal[habit_id] = dialog_goal.get_input()
    show_habit(habit_id)
    

# Buttons
create_habit_button = custom.CTkButton(master=app,
                            text="Create\n Habit",
                            text_color="Black",
                            width=70,
                            height=70,
                            command= lambda: show_habit(1))
create_habit_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

instructions_button = custom.CTkButton(master=app,
                            text="Instructions",
                            text_color="Black")
instructions_button.place(relx=0.1, rely=0.8, anchor=tk.CENTER)

settings_button = custom.CTkButton(master=app,
                            text="Settings",
                            text_color="Black")
settings_button.place(relx=0.1, rely=0.87, anchor=tk.CENTER)

exit_button = custom.CTkButton(master=app,
                            text="Exit",
                            text_color="Firebrick",
                            fg_color="Black",
                            border_color="Firebrick",
                            border_width=2,
                            hover_color = "black",
                            command=exit)
exit_button.place(relx=0.1, rely=0.94, anchor=tk.CENTER)


# Habit 1
name_label_1 = custom.CTkLabel(master=app, 
                            width=100,
                            height=28,
                            text=str(habit_name[1]),
                            text_color="Black",
                            fg_color=("darkcyan"),
                            corner_radius=7)
name_label_1.place(relx=0.14, rely=0.08, anchor=tk.CENTER)


goal_label_1 = custom.CTkLabel(master=app,
                            width=100,
                            height=28,
                            text="Goal: " + str(habit_goal[1]),
                            text_color="Black",
                            fg_color=("lightpink"),
                            corner_radius=7)
goal_label_1.place(relx=0.14, rely=0.14, anchor=tk.CENTER)


progress_label_1 = custom.CTkLabel(master=app,
                            width=100,
                            height=28,
                            text="Progress: " + str(habit_progress[1]) + "%",
                            text_color="Black",
                            fg_color=("slateblue"),
                            corner_radius=7)
progress_label_1.place(relx=0.14, rely=0.2, anchor=tk.CENTER)


check_var = custom.StringVar(value="on")
complete_habit_button_1 = custom.CTkCheckBox(master = app,
                            text = "", 
                            width = 26,
                            height = 26,
                            checkbox_width = 26,
                            checkbox_height = 26,
                            border_color = "white", 
                            command = lambda: update_progress(1),
                            variable=check_var, 
                            onvalue="on", 
                            offvalue="off")
complete_habit_button_1.place(relx=0.21, rely=0.28, anchor=tk.CENTER)


edit_icon = custom.CTkImage(light_image=Image.open("Edit Icon.png"), size = (15, 15))

edit_habit_button_1 = custom.CTkButton(master=app,
                            image = edit_icon,
                            text="",
                            width=25,
                            height=25,
                            fg_color="White",
                            hover_color="LightGrey")
edit_habit_button_1.place(relx=0.145, rely=0.28, anchor=tk.CENTER)


delete_icon = custom.CTkImage(light_image=Image.open("Delete Icon.png"), size = (15, 15))

delete_habit_button_1 = custom.CTkButton(master=app,
                            image = delete_icon,
                            text = '',
                            width = 25,
                            height = 25,
                            fg_color = "Firebrick",
                            hover_color = "Orangered",
                            command = lambda: delete(1))
delete_habit_button_1.place(relx=0.08, rely=0.28, anchor=tk.CENTER)


app.mainloop()