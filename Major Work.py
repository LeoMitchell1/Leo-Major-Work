import customtkinter as custom
import tkinter as tk


#Creates main app window
app = custom.CTk()
app.title("Habit Tracker")
app.geometry('600x600')
app.resizable(False, False)

custom.set_appearance_mode("dark")


#Initialises habit variables
habit_name = {1: "Habit 1", 2: "Habit 2"}
habit_goal = {1: 7}
habit_progress = {1: 0}
habit_increment = {1: 1}
habit_completed = {1: False}

#Function for exit button
def exit():
    quit()

#Function for updating habit progress
def update_progress(habit_id):
    if habit_progress[habit_id] < habit_goal[habit_id]:
        habit_progress[habit_id] += habit_increment[habit_id]
        habit_percentage = (habit_progress[habit_id]/habit_goal[habit_id])
        progress_label.configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
        if  habit_progress[habit_id] >= habit_goal[habit_id]:
            progress_label.configure(text="Habit Completed!")
















#Buttons
create_habit_button = custom.CTkButton(master=app,
                            text="Create\n Habit",
                            text_color="Black",
                            width=70,
                            height=70)
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
                            command=exit)
exit_button.place(relx=0.1, rely=0.94, anchor=tk.CENTER)


#Habit 1
name_label = custom.CTkLabel(master=app, 
                            width=100,
                            height=28,
                            text=str(habit_name[1]),
                            text_color="Black",
                            fg_color=("darkcyan"),
                            corner_radius=7)
name_label.place(relx=0.14, rely=0.08, anchor=tk.CENTER)

goal_label = custom.CTkLabel(master=app,
                            width=100,
                            height=28,
                            text="Goal: " + str(habit_goal[1]),
                            text_color="Black",
                            fg_color=("lightpink"),
                            corner_radius=7)
goal_label.place(relx=0.14, rely=0.14, anchor=tk.CENTER)

progress_label = custom.CTkLabel(master=app,
                            width=100,
                            height=28,
                            text="Progress: " + str(habit_progress[1]) + "%",
                            text_color="Black",
                            fg_color=("slateblue"),
                            corner_radius=7)
progress_label.place(relx=0.14, rely=0.2, anchor=tk.CENTER)

complete_habit_button = custom.CTkButton(master=app,
                            text="Complete Habit",
                            text_color="Black",
                            width=110,
                            height=35,
                            fg_color="Seagreen",
                            hover_color="Palegreen",
                            command=lambda: update_progress(1))
complete_habit_button.place(relx=0.14, rely=0.28, anchor=tk.CENTER)

edit_habit_button = custom.CTkButton(master=app,
                            text="Edit Habit",
                            text_color="Black",
                            width=110,
                            height=35,
                            fg_color="White",
                            hover_color="LightGrey")
edit_habit_button.place(relx=0.14, rely=0.35, anchor=tk.CENTER)


app.mainloop()