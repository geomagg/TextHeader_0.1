import tkinter as tk
from tkinter import filedialog

from segysak.segy import get_segy_texthead
from segysak.segy import create_default_texthead
from segysak.segy import put_segy_texthead
from segysak.segy import get_segy_texthead

#from parse_text_header import parse_text_header  
import matplotlib.pyplot as plt
import pathlib

root = tk.Tk()
root.title("SEGY TEXT HEADER EDITOR")

def new_file():
    text.delete("1.0", tk.END)
    root.title("SEGY Text Header Editor")

def open_segy():
    global ebcdic, filesegy
    file_segy = filedialog.askopenfilename(defaultextension=".segy", filetypes=[("SEGY FILES", "*.sgy"), ("All Files", "*.*")])
    filesegy = pathlib.Path(file_segy)
    ebcdic=get_segy_texthead(filesegy, ext_headers=False, no_richstr=False)
    text.delete("1.0", tk.END)
    text.insert(tk.END, ebcdic)
    root.title(file_segy)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = text.get("1.0", tk.END)
            file.write(content)
        root.title(file_path)

        
def save_segy():
    file_path = filedialog.asksaveasfilename(defaultextension=".sgy", filetypes=[("SGY Files", "*.segy"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content= put_segy_texthead(filesegy, ebcdic)
            file.write(filesegy)
#            print (get_segy_texthead(filesegy))
        root.title(file_path)




text = tk.Text(root, wrap="word", undo=True)
text.pack(expand="yes", fill="both")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="SEGY IO", menu=file_menu)
file_menu.add_command(label="Open", command=open_segy)
file_menu.add_command(label="Save EBCDIC HEADER", command=save_file)
file_menu.add_command(label="Save SEGY FILE", command=save_segy)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

file_menu1 = tk.Menu(menu_bar, tearoff=0)
#menu_bar.add_cascade(label="EBCDIC HEADER", menu=file_menu1)
#file_menu1.add_command(label="Open", command=open_file)
#file_menu1.add_command(label="Save", command=save_file)


root.mainloop()
