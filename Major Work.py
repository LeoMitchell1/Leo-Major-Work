import customtkinter as custom
import tkinter as tk



#Habit 3
habit3_name = 'null'
habit3_goal = 0
habit3_progress = 0
habit3_date = '3/4/2024'
habit3_completed = False


def habit_1():
    global habit1_increment

    habit1_name = 'null'
    habit1_goal = 0
    habit1_progress = 0
    habit1_increment = 0.1
    habit1_date = '3/4/2024'
    habit1_completed = False

    print("Name:", habit1_name)
    print("Goal:", habit1_goal)
    print("Progress Name:", habit1_progress)
    print("Date Created:", habit1_date)
    print("Habit Name:", habit1_completed)

    habit1_name = input("New name: ")
    habit1_goal = input("New goal: ")

def update_progress1():
    habit1_progress += habit1_increment


main_window = tk.Tk()
main_window.title("Habit Tracker")
main_window.geometry('600x600')
main_window.resizable(False, False)

canvas_width = 600
canvas_height = 600

c = tk.Canvas(main_window, width=canvas_width, height=canvas_height, bg='white')
c.pack()


button = custom.CTkButton(main_window, fg_color="red", text="Update Habit 1", command=habit_1)
button.place(relx=0.5, rely=0.47, anchor=tk.CENTER)


main_window.mainloop()