import customtkinter as custom
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import *
from PIL import Image


# Fully create all 8 habits
# Write instructions and create pop up window
# Improve the UI (try removing background colour of labels, adding border colour to frame)
# Make appearance window remember the current appearance state
# Add habit categories (list them at bottom of screen, colour code them with frame borders)



# Creates main app window
app = custom.CTk()
app.title("Habit Tracker")
app.geometry('680x600+650+200')
app.resizable(False, False)
custom.set_appearance_mode("dark")
custom.set_default_color_theme("green")


# Initialises habit variables
habit_name = {1: "Habit 1", 2: "Habit 2", 3: "Habit 3", 4: "Habit 4", 5: "Habit 5", 6: "Habit 6", 7: "Habit 7", 8: "Habit 8"}
habit_goal = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7:0, 8:0}
habit_progress = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7:0, 8:0}
habit_completed = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False}
habit_counter = 0
appearance_label = None
background = "#242424"
frame = "#2b2b2b"


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


# Function for delete button
def delete_button(habit_id):
    global habit_counter
    if habit_id == 1:
        name_label_1.grid_forget()
        goal_label_1.grid_forget()
        progress_label_1.grid_forget()
        progressbar_1.grid_forget()
        complete_habit_button_1.grid_forget()
        edit_habit_button_1.grid_forget()
        delete_habit_button_1.grid_forget()
    elif habit_id == 2:
        name_label_2.grid_forget()
        goal_label_2.grid_forget()
        progress_label_2.grid_forget()
        progressbar_2.grid_forget()
        complete_habit_button_2.grid_forget()
        edit_habit_button_2.grid_forget()
        delete_habit_button_2.grid_forget()  
    habit_name[habit_id] = ""
    habit_progress[habit_id] = 0
    habit_counter -= 1  


# Function for changing appearance
def change_appearance(new_appearance):
    global appearance_label
    custom.set_appearance_mode(new_appearance)
    if custom.get_appearance_mode() == "Dark":
        appearance_label.configure(text_color = "White")
    else:
        appearance_label.configure(text_color = "Black")


# Function for settings button
def settings_button():
    global appearance_label
    settings_window = custom.CTkToplevel(app)
    settings_window.title("Settings")
    settings_window.geometry('400x200+750+300')
    settings_window.resizable(False, False)
    settings_window.attributes('-topmost', True)

    appearance_label = custom.CTkLabel(master=settings_window,
                                        text="Appearance:",
                                        text_color=("White"))
    appearance_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    save_button = custom.CTkButton(master=settings_window,
                                    text="Save",
                                    text_color="Black",
                                    width=80,
                                    command = settings_window.destroy)
    save_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    appearance_menu = custom.CTkOptionMenu(settings_window,
                                values=["Dark", "Light", "System"],
                                command = change_appearance)
    appearance_menu.place(relx=0.5, rely=0.4, anchor=tk.CENTER)


# Function for updating habit progress
def update_progress(habit_id):
    global check_var_1, check_var_2

    if habit_id == 1:
        checkbox = check_var_1.get()
    elif habit_id == 2:
        checkbox = check_var_2.get()

    if checkbox == 'on':
        if (habit_progress[habit_id]) < int(habit_goal[habit_id]):
            habit_progress[habit_id] += 1
            habit_percentage = (habit_progress[habit_id]/int(habit_goal[habit_id]))
            if habit_id == 1:  
                progress_label_1.configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
                progressbar_1.set(habit_percentage)
            elif habit_id == 2:
                progress_label_2.configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
                progressbar_2.set(habit_percentage)
            if habit_progress[habit_id] >= int(habit_goal[habit_id]):
                if habit_id == 1:
                    progress_label_1.configure(text="Completed!")
                elif habit_id == 2:
                    progress_label_2.configure(text="Completed!")
                habit_completed[habit_id] = True
    if checkbox == 'off':
        if habit_progress[habit_id] > 0:
            habit_progress[habit_id] -= 1
            habit_percentage = (habit_progress[habit_id]/int(habit_goal[habit_id]))
            if habit_id == 1:
                progress_label_1.configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
                progressbar_1.set(habit_percentage)
            elif habit_id == 2:
                progress_label_2.configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
                progressbar_2.set(habit_percentage)
            if habit_progress[habit_id] < int(habit_goal[habit_id]):
                if habit_id == 1:
                    progress_label_1.configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
                elif habit_id == 2:
                    progress_label_2.configure(text="Progress: " + (f"{(habit_percentage):.0%}"))
                habit_completed[habit_id] = False


# Updates habit buttons and labels
def update_habit(habit_id):
    if habit_id == 1:
        name_label_1.configure(text= str(habit_name[habit_id]))
        goal_label_1.configure(text="Goal: " + str(habit_goal[1]) + "/w")
        progress_label_1.configure(text="Progress: " + str(habit_progress[habit_id]) + "%")
        progressbar_1.set(habit_progress[habit_id])
    elif habit_id == 2:
        name_label_2.configure(text= str(habit_name[habit_id]))
        goal_label_2.configure(text="Goal: " + str(habit_goal[1]) + "/w")
        progress_label_2.configure(text="Progress: " + str(habit_progress[habit_id]) + "%")
        progressbar_2.set(habit_progress[habit_id])


# Function for showing a new habit
def show_habit(habit_id):
    if habit_id == 1:
        name_label_1.grid(row=0, column=0, padx=15, pady=(18, 5), sticky = "we")
        goal_label_1.grid(row=1, column=0, padx=15, pady=5,  sticky = "we")
        progress_label_1.grid(row=2, column=0, padx=15, pady=5,  sticky = "we")
        progressbar_1.grid(row=3, column=0, padx=15, pady=5,  sticky = "we")
        complete_habit_button_1.grid(row=4, column=0, padx=(5,10), pady=5, sticky = "e")
        edit_habit_button_1.grid(row=4, column=0, padx=(5,5), pady=5)
        delete_habit_button_1.grid(row=4, column=0, padx=(15,0), pady=5, sticky = "w")


# Function for edit button
def edit_habit(habit_id):
    while True:
        dialog_name = custom.CTkInputDialog(text="Please enter the name of the habit: ")
        dialog_name.geometry('325x175+875+500')
        placehold_name = dialog_name.get_input()
        if placehold_name == "" or placehold_name == None:
            break
        elif len(placehold_name) > 12:
            messagebox.showerror("Error", "Please enter a name shorter than 12 characters.")
        else:
            habit_name[habit_id] = placehold_name
            break
    
    while True:
        dialog_goal = custom.CTkInputDialog(text="How many times do you aim to complete this habit per week? ")
        dialog_goal.geometry('325x175+875+500')
        placehold_goal = dialog_goal.get_input()
        if placehold_goal == "" or placehold_goal == None:
            break
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
    global habit_counter
    habit_id = habit_counter + 1
    while True:
        dialog_name = custom.CTkInputDialog(text="Please enter the name of the habit: ")
        dialog_name.geometry('325x175+875+500')
        dialog_name.title("Create Habit")
        placehold_name = dialog_name.get_input()
        if placehold_name == "" or placehold_name == None:
            break
        elif len(placehold_name) > 12:
            messagebox.showerror("Error", "Please enter a name shorter than 12 characters.")
        else:
            habit_name[habit_id] = placehold_name
            break
    
    while True:
        dialog_goal = custom.CTkInputDialog(text="How many times do you aim to complete this habit per week? ")
        dialog_goal.geometry('325x175+875+500')
        dialog_goal.title("Create Goal")
        placehold_goal = dialog_goal.get_input()
        if placehold_goal == "" or placehold_goal == None:
            break
        elif placehold_goal.isnumeric() == False:
            messagebox.showerror("Error", "Please enter a number.")
        elif int(placehold_goal) > 20:
            messagebox.showerror("Error", "Please enter a number less than 20.")
        else:
            habit_goal[habit_id] = placehold_goal
            break

    habit_progress[habit_id] = 0
    habit_counter += 1
    update_habit(habit_id)
    show_habit(habit_id)
    

# Buttons
create_habit_button_ = custom.CTkButton(master=app,
                            text="Create\n Habit",
                            text_color="Black",
                            width=70,
                            height=70,
                            command = create_habit)
create_habit_button_.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

instructions_button = custom.CTkButton(master=app,
                            text="Instructions",
                            text_color="Black")
instructions_button.place(relx=0.1, rely=0.8, anchor=tk.CENTER)

settings_button = custom.CTkButton(master=app,
                            text="Settings",
                            text_color="Black",
                            command = settings_button)
settings_button.place(relx=0.1, rely=0.87, anchor=tk.CENTER)

exit_button = custom.CTkButton(master=app,
                            text="Exit",
                            text_color="White",
                            fg_color = "Firebrick",
                            hover_color = "black",
                            command=exit_button)
exit_button.place(relx=0.1, rely=0.94, anchor=tk.CENTER)


# Habit 1
habit_1_frame = custom.CTkFrame(app, width=150, height=200, border_color = 'aquamarine', border_width = 2)
habit_1_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
habit_1_frame.columnconfigure(30)

name_label_1 = custom.CTkButton(master=habit_1_frame, 
                            width=120,
                            height=28,
                            text=str(habit_name[1]),
                            text_color="White",
                            border_color = "White",
                            border_width = 2,
                            fg_color = (frame),
                            corner_radius=7)


goal_label_1 = custom.CTkButton(master=habit_1_frame,
                            width=100,
                            height=28,
                            text = "Goal: " + str(habit_goal[1]) + "/w",
                            text_color="White",
                            border_color = "White",
                            border_width = 2,
                            fg_color = (frame),
                            corner_radius=7)

progress_label_1 = custom.CTkButton(master=habit_1_frame,
                            width=100,
                            height=28,
                            text="Progress: " + str(habit_progress[1]) + "%",
                            text_color="White",
                            border_color = "White",
                            border_width = 2,
                            fg_color = (frame),
                            corner_radius=7)

progressbar_1 = custom.CTkProgressBar(habit_1_frame, 
                            orientation="horizontal",
                            width = 100,
                            height = 15,
                            progress_color = "white",
                            )
progressbar_1.set(0)

check_var_1 = custom.StringVar(value="off")
complete_habit_button_1 = custom.CTkCheckBox(habit_1_frame,
                            text = "", 
                            width = 26,
                            height = 26,
                            checkbox_width = 26,
                            checkbox_height = 26,
                            border_color = "white", 
                            command = lambda: update_progress(1),
                            variable=check_var_1, 
                            onvalue="on", 
                            offvalue="off")

edit_icon = custom.CTkImage(light_image=Image.open("Edit Icon.png"), size = (15, 15))
edit_habit_button_1 = custom.CTkButton(habit_1_frame,
                            image = edit_icon,
                            text="",
                            width=25,
                            height=25,
                            fg_color="White",
                            hover_color="LightGrey",
                            command = lambda: edit_habit(1))

delete_icon = custom.CTkImage(light_image=Image.open("Delete Icon.png"), size = (15, 15))
delete_habit_button_1 = custom.CTkButton(habit_1_frame,
                            image = delete_icon,
                            text = '',
                            width = 25,
                            height = 25,
                            fg_color = "Firebrick",
                            hover_color = "Orangered",
                            command = lambda: delete_button(1))


# Habit 2
habit_2_frame = custom.CTkFrame(app, width=150, height=200)
habit_2_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


name_label_2 = custom.CTkLabel(master=app, 
                            width=100,
                            height=28,
                            text=str(habit_name[1]),
                            text_color="Black",
                            fg_color=("darkcyan"),
                            corner_radius=7)

goal_label_2 = custom.CTkLabel(master=app,
                            width=100,
                            height=28,
                            text="Goal: " + str(habit_goal[1]),
                            text_color="Black",
                            fg_color=("lightpink"),
                            corner_radius=7)

progress_label_2 = custom.CTkLabel(master=app,
                            width=100,
                            height=28,
                            text="Progress: " + str(habit_progress[1]) + "%",
                            text_color="Black",
                            fg_color=("slateblue"),
                            corner_radius=7)

progressbar_2 = custom.CTkProgressBar(app, 
                            orientation="horizontal",
                            width = 100,
                            height = 10,
                            progress_color = "slateblue",
                            )
progressbar_2.set(0)

check_var_2 = custom.StringVar(value="on")
complete_habit_button_2 = custom.CTkCheckBox(master = app,
                            text = "", 
                            width = 26,
                            height = 26,
                            checkbox_width = 26,
                            checkbox_height = 26,
                            border_color = "white", 
                            command = lambda: update_progress(2),
                            variable=check_var_2, 
                            onvalue="on", 
                            offvalue="off")

edit_icon = custom.CTkImage(light_image=Image.open("Edit Icon.png"), size = (15, 15))
edit_habit_button_2 = custom.CTkButton(master=app,
                            image = edit_icon,
                            text="",
                            width=25,
                            height=25,
                            fg_color="White",
                            hover_color="LightGrey",
                            command = lambda: edit_habit(2))

delete_icon = custom.CTkImage(light_image=Image.open("Delete Icon.png"), size = (15, 15))
delete_habit_button_2 = custom.CTkButton(master=app,
                            image = delete_icon,
                            text = '',
                            width = 25,
                            height = 25,
                            fg_color = "Firebrick",
                            hover_color = "Orangered",
                            command = lambda: delete_button(2))


# Habit 3
habit_3_frame = custom.CTkFrame(app, width=150, height=200)
habit_3_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")


# Habit 4
habit_4_frame = custom.CTkFrame(app, width=150, height=200)
habit_4_frame.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")


# Habit 5
habit_5_frame = custom.CTkFrame(app, width=150, height=200)
habit_5_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


# Habit 6
habit_6_frame = custom.CTkFrame(app, width=150, height=200)
habit_6_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")


# Habit 7
habit_7_frame = custom.CTkFrame(app, width=150, height=200)
habit_7_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")


# Habit 8
habit_8_frame = custom.CTkFrame(app, width=150, height=200)
habit_8_frame.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")


app.mainloop()