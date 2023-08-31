import tkinter as tk
from tkinter import ttk
from datetime import datetime

class panel:

    def __init__(self,items):
        self.items = items
        self.objects = []
        self.ncols = 6

    def displayitems(self,root):
        for i in range(len(self.items)):
            if self.items[i].completed:
                continue
            if self.items[i].priority == "High":
                bg = '#d93232'
            elif self.items[i].priority == "Medium":
                bg = '#d9c032'
            else:
                bg = '#32d96c'
            # color the row
            titleframe = tk.Frame(root, bg=bg)
            t0 = titleframe
            titleframe.grid(row=i+1,column=1,columnspan=3, sticky='news')
            # add the details about the item
            t1 = tk.Label(root,text=self.items[i].title,justify="left",anchor="w",bg=bg)
            t2 = tk.Label(root,text=self.items[i].due,justify="left",anchor="w",bg=bg)
            t3 = tk.Label(root,text=self.items[i].priority,justify="left",anchor="w",bg=bg)
            self.objects.append(t0)
            self.objects.append(t1)
            self.objects.append(t2)
            self.objects.append(t3)
            t1.grid(sticky=tk.W,row=i+1,column=1)
            t2.grid(sticky=tk.W,row=i+1,column=2)
            t3.grid(sticky=tk.W,row=i+1,column=3)
            # add slider
            s1 = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL,value=self.items[i].progress)
            self.items[i].add_slider(s1)
            s1.grid(sticky=tk.W,row=i+1,column=4)
            self.objects.append(s1)
            # add the buttons
            buttonDONE = tk.Button(root,text="Done",padx=0,pady=0,command=self.items[i].done,bg=bg)
            buttonEDIT = tk.Button(root,text="Edit",padx=0,pady=0,command=self.items[i].edit,bg=bg)
            buttonDEL = tk.Button(root,text="Delete",padx=0,pady=0,command=self.items[i].delete,bg=bg)
            buttonDONE.grid(row=i+1,column=0)
            buttonEDIT.grid(row=i+1,column=5)
            buttonDEL.grid(row=i+1,column=6)
            self.objects.append(buttonDONE)
            self.objects.append(buttonEDIT)
            self.objects.append(buttonDEL)

    def additem(self,root):
        # open dialogue window to create item
        addroot = tk.Tk()
        addroot.title("Add item")
        addroot.geometry("400x400")
        # enter title, due date, priority: create fields then read from entries
        tk.Label(addroot, text="Title", justify="left", anchor="w").grid(sticky = tk.W, row=0)
        tk.Label(addroot, text="Due (dd/mm/yyyy)", justify="left", anchor="w").grid(sticky = tk.W, row=1)
        tk.Label(addroot, text="Priority (Low/Medium/High)", justify="left", anchor="w").grid(sticky = tk.W, row=2)
        tk.Label(addroot, text="Details", justify="left", anchor="w").grid(sticky = tk.W, row=3)
        e1 = tk.Entry(addroot)
        e2 = tk.Entry(addroot)
        e3 = tk.Entry(addroot)
        e4 = tk.Text(addroot,height=10,width=30)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        def create():
            title = e1.get()
            due = e2.get()
            priority = e3.get()
            details = e4.get("1.0", tk.END)
            # added and completed are set automatically
            added = datetime.now().strftime("%d/%m/%Y")
            completed = False
            Item = todoitem(title,added,due,completed,priority,0,details,root)
            Item.add_panel(self)
            # insert the new item at the right place
            iloc = 0
            for i in range(len(self.items)):
                if (self.items[i] < Item):
                    break
                iloc = i+1
            self.items.insert(iloc,Item)
            addroot.destroy()
            # add the new text
            for i in self.objects:
                i.destroy()
            self.displayitems(root)
        bENTER = tk.Button(addroot,text="Create",padx=0,pady=0,command=create)
        bENTER.place(x=150,y=250)
        tk.mainloop()

class todoitem:

    def __init__(self,title,added,due,completed,priority,progress,details,root):
        self.title = title
        self.added = added
        self.due = due
        self.completed = completed
        self.priority = priority
        self.root = root
        self.progress = progress
        self.details = details

    def add_panel(self,panel):
        self.panel = panel

    def add_slider(self,slider):
        self.slider = slider

    def done(self):
        self.completed = True
        self.panel.items.remove(self)
        for i in self.panel.objects:
            i.destroy()
        self.panel.displayitems(self.root)

    def delete(self):
        self.panel.items.remove(self)
        for i in self.panel.objects:
            i.destroy()
        self.panel.displayitems(self.root)

    def edit(self):
        # open new window (same as additem)
        addroot = tk.Tk()
        addroot.title("Edit item")
        addroot.geometry("400x400")

        # put same entry fields but with existing text
        tk.Label(addroot, text="Title", justify="left", anchor="w").grid(sticky = tk.W, row=0)
        tk.Label(addroot, text="Due (dd/mm/yyyy)", justify="left", anchor="w").grid(sticky = tk.W, row=1)
        tk.Label(addroot, text="Priority (Low/Medium/High):", justify="left", anchor="w").grid(sticky = tk.W, row=2)
        # tk.Label(addroot, text="Details", justify="left", anchor="w").grid(sticky = tk.W, row=3)
        e1 = tk.Entry(addroot)
        e2 = tk.Entry(addroot)
        e3 = tk.Entry(addroot)
        e4 = tk.Text(addroot,height=10,width=30)
        e1.insert(0,self.title)
        e2.insert(0,self.due)
        e3.insert(0,self.priority)
        e4.insert("1.0",self.details)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)

        # read new entries and update position in list
        def create():
            changed = False
            if (e1.get() != self.title or e2.get() != self.due or e3.get() != self.priority or e4.get("1.0", tk.END) != self.details):
                changed = True
            if changed:
                # move the item to its new position
                # remove the item from the list
                self.panel.items.remove(self)
                self.title = e1.get()
                self.due = e2.get()
                self.priority = e3.get()
                self.details = e4.get("1.0", tk.END)
                # insert the new item at the right place
                iloc = 0
                for i in range(len(self.panel.items)):
                    if (self.panel.items[i] < self):
                        break
                    iloc = i+1
                self.panel.items.insert(iloc,self)
                addroot.destroy()
                # add the new text
                for i in self.panel.objects:
                    i.destroy()
                self.panel.displayitems(self.root)

        # button "create"
        bENTER = tk.Button(addroot,text="Create",padx=0,pady=0,command=create)
        bENTER.place(x=150,y=250)
        # run
        addroot.mainloop()


    def __eq__(self,other):
        return ((self.title,self.added,self.due,self.completed,self.priority,self.details)) == ((other.title,other.added,other.due,other.completed,other.priority,other.details))
    
    def __gt__(self,other):
        if (self.priority == other.priority):
            if int(self.due[6:]) < int(other.due[6:]):
                return True
            elif int(self.due[3:5]) < int(other.due[3:5]):
                return True
            elif int(self.due[0:2]) < int(other.due[0:2]):
                return True
            else:
                return False
        else:
            if self.priority == "High":
                return True
            elif other.priority == "High":
                return False
            elif self.priority == "Medium":
                return True
            else:
                return False