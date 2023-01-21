import os
import tkinter as tk
from tkinter import messagebox

class askstring():
    def __init__(self, root, title, message):
        self.toreturn = ''
        self.w = tk.Toplevel(root)
        self.w.title(title)
        tk.Label(self.w, text=message).pack(expand=True, fill='y', side='top')
        self.e = tk.Entry(self.w)
        self.e.pack(expand=True, fill='y')
        self.e.focus()
        self.w.bind('<Return>', lambda evt: self.clickedtrue(self))
        tk.Button(self.w, text="OK", command=lambda: self.clickedtrue(self)).pack(expand=True, fill='y', side='bottom')
        root.wait_window(self.w)
        self.value = self.toreturn
    def __str__(self):
        return self.toreturn
    def clickedtrue(self, event=None):
        self.toreturn = self.e.get()
        self.w.destroy()
        
# read the json file with all widgets
widgets = []
if os.path.exists('widget'):
    for filename in os.listdir('widget'):
        f = os.path.join("widget\\", filename)
        # checking if it is a file
        if os.path.isfile(f):
            widgets.append(filename[:filename.rfind('.')])
else:
    os.mkdir('widget')

root = tk.Tk()
root.title('PY Widget Maker')
root.geometry('700x300')

# the name of the current widget
name = "New"

# insert all created widgets in the list
listbox = tk.Listbox(root)
listbox.pack(expand=1, fill='both', side='top')
for i in widgets:
    listbox.insert('end', str(i))
# insert the element 'new' that creates a new widget
listbox.insert('end', 'New')
listbox.selection_set(0, 0)

def save_config(code, master):
    global widgets, listbox, name
    #try:
    if name == 'New':
        name = askstring(master, 'Name', 'Enter Widget\'s name').__str__()
        widgets.append(name)
    with open(f'widget\{name}.pyw', 'w') as f:
        f.write(code.get(0.0, 'end'))
    listbox.delete(0, 'end')
    for i in widgets:
        listbox.insert('end', str(i))
    listbox.insert('end', 'New')
    listbox.selection_set(0, 0)
    master.destroy()
    #except:
    #    messagebox.showerror(title="Error", message="An error occured.\nTry to select the widget you want to configure in the listbox")

def deleteWidget():
    global widgets, listbox, name
    name = listbox.selection_get()
    widgets.pop(widgets.index(name))
    os.remove(f"widget\{name}.pyw")
    listbox.delete(0, 'end')
    for i in widgets:
        listbox.insert('end', str(i))
    listbox.insert('end', 'New')
    listbox.selection_set(0, 0)
        
def configureWidget():
    global name
    name = listbox.selection_get()
    config_win = tk.Toplevel(root)
    config_win.title('Configure a Widget')
    config_win.geometry('500x700')
    code = tk.Text(config_win)
    if name != 'New':
        with open(f"widget\{name}.pyw", 'r') as f:
            code.insert(0.0, f.read())
    code.pack(expand=1, fill='both', side='top')
    save = tk.Button(config_win, text='save', command= lambda: save_config(code, config_win))
    save.pack(expand=1, fill='x', side='bottom')

div = tk.Frame(root)
div.pack(expand=1, fill='x', side='bottom')
button = tk.Button(div, text="Configure", command=configureWidget)
button.pack(expand=1, fill='x', side='top')
button2 = tk.Button(div, text="Delete", command=deleteWidget)
button2.pack(expand=1, fill='x', side='bottom')

root.mainloop()
