# Developer Notes

## TO DOs

1. Write instructions and create pop up window for it
2. Improve the UI - Design features (try removing background colour of labels, adding border colour to frame)
3. Add habit categories (list them at bottom of screen, colour code them with frame borders, make little colour squares appear in the calendar frames that it was completed)
4. Create calendar tracking window with stats (optional)
6. Make the appearance remember what it is set to when you close and reopen
7. Go through and optimise the code, removing duplicates, simplifying functions etc.
10. Make the progress for each habit save when the day changes, the checkbox will then reset to default to allow for the next progression
11. Write README file contents
12. Go through and add comments explaining everything

## Completed

* Go through and do Error management for all inputs (7/4)
* Add a dialog window for exit confirmation (7/4)
* Do the create habit dialog window (7/4)
* Do the edit habit dialog window (7/4)
* Setup settings with light mode and dark mode (7/4)
* Fix grid placement/padding (7/4)
* Make it so that deleting a habit sets its name to Habit + Habit_id instead of blank (18/5)
* Add a daily calendar function at the top (18/5)
* Add habit category functionality using frame borders (20/5)
* Change the pop up windows for create and edit habit to be all in one window, using entry fields instead of dialog boxes (21/5)
* Make it so that the indicators only show when a habit has been checked (24/5)
* Make the calendar indicators save and shuffle to the left as the days change (16/6)

## Problems

1. Fix the error with the habit percentage not accepting nan (12/5)
2. Fix the isnumeric error not accepting NoneType (12/5)
3. inside_create function running even without the button being pressed (20/5)
4. habit_name and habit_category not being updated when creating a new habit (20/5)
5. When creating a new habit when there is no available habit slot, the create habit window still opens and the error message appears behind it. (20/5)
6. After deleting a habit, the indicator in the calendar doesn't line up properly (21/5)
7. If name is null, closing and reopening causes it to be named NaN (7/6)
8. When you edit a habit without changing the name an error pops up (Make it so that if the name field is empty it will still edit but nothing will change) (7/6)
9. Editing a habit makes the indicator automatically turn on when it shouldn't (7/6)
10. Habit label font colours are light grey when in light mode (12/6)
11. Habit checkbox would remain on if the habit was deleted and then recreated (10/6)
12. The indication history is displaying in the opposite order, the order needs to be inverted (16/6)

## Solutions

1. Made it so that there was no situation where nan was a value for goal or progress (15/5)
2. Separated the error checking so that it checks for NoneType errors first and then closes the dialog (15/5)
3. There was parenthesis at the end of the command, used a lambda function to fix this (20/5)
4. When retrieving the value for habit_name, there was a entry called habit_name as well as a dictionary, this caused an issue as the wrong value was being retrieved. I changed the value of the entryfield which fixed the issue. I also updated the write_csv() so that the habit_category would update correctly. (20/5)
5. Moved the error checking to before the creation of the window (20/5)
6. Added each check frame to a dictionary so that its positioned can be changed and saved in the correct order. (24/5)
7. Added an error check if the name is null to show an error box (7/6)
8. 
9. Implemented the create variable from the create habit function and changed it to edit and used it for both (7/6)
10. Added an if statement after changing the theme to change the text and border colour to the correct colour (16/6)
11. Added an if statement when deleting or reseting a habit to toggle the checkbox to false (13/6)