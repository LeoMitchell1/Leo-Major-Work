import customtkinter as custom
import tkinter as tk


main_window = tk.Tk()
main_window.title("Habit Tracker")
main_window.geometry('600x600')
main_window.resizable(False, False)

canvas_width = 600
canvas_height = 600

c = tk.Canvas(main_window, width=canvas_width, height=canvas_height, bg='white')
c.pack()

button = custom.CTkButton(main_window, fg_color="red", text="Create Habit")
button.place(relx=0.5, rely=0.47, anchor=tk.CENTER)





class Habit:
    def __init__(self, name, goal):
        self.name = []
        self.goal = []
        self.completed = []

def create_habit():
        name = input("Enter the name of the habit: ")
        goal = int(input("Enter the goal number of times to complete the habit: "))
        print(name, "habit created!")
        return Habit(name, goal)

def show_habit(self):
        print("Habit name:", self.name)
        print("Habit goal:", self.goal)
        print("Habit completed:", self.completed)

def complete_habit(habit, date):
        date = input("What date did you complete this habit? ")
        habit.completed.append(date)

def check_progress(habit):
        check = input("What habit would you like to check? ")
        return len(habit.completed) / habit.goal * 100
        
        
main_window.mainloop()