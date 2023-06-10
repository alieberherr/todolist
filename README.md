# python-based to do list

## Necessary packages
- tkinter
- datetime
- os
- pandas

## How it works

The program can be launched by running `python gui.py`. When it is first called, an empty list will be opened with two buttons, 'x' and '+'.
Use '+' to add items to the list and 'x' to close the program.

Each item is given a title, a due date and a priority. The list will look something like this:
<img width="504" alt="Screenshot 2023-06-10 at 17 51 10" src="https://github.com/alieberherr/todolist/assets/91953198/2a02a777-5cf7-4c92-bd42-6904b5dd8657">

The items are sorted
(i) with respect to priority,
(ii) within each priority with respect to due date (early due dates are higher up) and
(iii) for the same due date they are ordered by the time that they were added (ealier added show up on top).

When the program is closed, all contents are written to a CSV file called `todod.csv`.
