# python-based to do list

## Necessary packages
- tkinter
- datetime
- os
- pandas

## How it works

The program can be launched by running `python gui.py`. When it is first called, an empty list will be opened with two buttons, 'x' and '+'.
Use '+' to add items to the list and 'x' to close the program.

Each item is given a title, a due date and a priority. There is also a slider to indicate the progress for each item. In the end, the list will look something like this:

<img width="599" alt="Example to-do list. It shows items with dummy names, coloured according to their priority." src="https://github.com/alieberherr/todolist/assets/91953198/3f287933-eb42-4e48-b67c-dc017dd0ed9b">

The items are sorted
(i) with respect to priority,
(ii) within each priority with respect to due date (early due dates are higher up) and
(iii) for the same due date they are ordered by the time that they were added (ealier added show up on top).

Items can be edited (button 'Edit'), deleted (button 'Delete') or marked as completed (button 'Done'). In the latter two cases, the item is removed from the list. So far, this action cannot be reversed. The Edit/Create buttons open the following window:

<img width="400" alt="Four fields, 'Title', 'Due date', Priority' and 'Details' where text can be entered. At the bottom is a button 'Create'." src="https://github.com/alieberherr/todolist/assets/91953198/47227f1b-1b8b-4878-a391-5540e9715366">

If an item is edited, the fields contain all previous information on the item. The only additional information in this window is the 'Details' field, which can be used to write down quick notes (IMPORTANT: do not use commas).

When the program is closed, all contents are written to a CSV file called `todos.csv`. Upon opening it the next time, the data will be read from the same file and the list is initialised accordingly.
