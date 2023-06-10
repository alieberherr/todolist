import tkinter as tk
from tkinter import ttk
import os
import panel
import pandas as pd

def init(second_frame):
    # read existing data from file
    items = []
    if (os.path.isfile("todos.csv")):
        df = pd.read_csv("todos.csv")
        # loop through the file and create instances of items
        for i,row in df.iterrows():
            Item = panel.todoitem(row["title"],row["added"],row["due"],row["completed"],row["priority"],second_frame)
            items.append(Item)
    Panel = panel.panel(items)
    return Panel

def run():
    root = tk.Tk()
    root.title("TODO")
    root.geometry("500x400")

    # create a main frame
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH,expand=1)

    # create a canvas
    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)

    # add a scrollbar
    my_scrollbar = ttk.Scrollbar(main_frame,orient=tk.VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    # create a frame inside the canvas
    second_frame = tk.Frame(my_canvas)

    # add that new frame to a window in the canvas
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")

    # # initialise panel and place text in 'root'
    Panel = init(second_frame)
    for i in Panel.items:
        i.add_panel(Panel)
    Panel.displayitems(second_frame)
    # add buttons "ADD" and "EXIT" to the top
    def add():
        Panel.additem(second_frame)
    def close():
        # write to file
        f = open("todos.csv",'w')
        f.write("title,added,due,completed,priority\n")
        for i in range(len(Panel.items)):
            Item = Panel.items[i]
            f.write("%s,%s,%s,%s,%s\n"%(Item.title,Item.added,Item.due,Item.completed,Item.priority))
        f.close()
        root.destroy()
    buttonADD = tk.Button(second_frame,text="+",padx=0,pady=0,command=add).grid(row=0,column=1)
    buttonEXIT = tk.Button(second_frame,text="x",command=close,padx=0,pady=0).grid(row=0,column=0)

    root.mainloop()

if __name__=="__main__":
    run()