import tkinter as tk
from tkinter import filedialog

from segysak.segy import get_segy_texthead
from segysak.segy import create_default_texthead
from segysak.segy import put_segy_texthead
from segysak.segy import get_segy_texthead
from segysak.segy import segy_bin_scrape


from CTkMessagebox import CTkMessagebox

import matplotlib.pyplot as plt
import pathlib

root = tk.Tk()
root.title("SEGY TEXT HEADER EDITOR")


def show_error():
    # Show some error message
    CTkMessagebox(title="Error", message="SEGY FILE NOT read!!!", icon="cancel")


def new_file():
    text.delete("1.0", tk.END)
    root.title("SEGY Header Manipulation")

def open_file():
    text.delete("1.0", tk.END)
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            ebcdic = file.read()
            print (ebcdic)
            text.delete("1.0", tk.END)
            text.insert(tk.END, ebcdic)
        root.title(file_path)


def open_segy():
    text.delete("1.0", tk.END)
    global  filesegy, ebcdic
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
            CTkMessagebox(title="Saved File", icon="check.png",
                  message="EBCDIC FILE saved:")
            text.delete("1.0", tk.END)
        root.title(file_path)

        
def save_segy():
   if 'filesegy' in globals():
     content = text.get("1.0", tk.END)
     put_segy_texthead(filesegy, content)
     root.title("Saving in SEGY TEXT HEADER")
     CTkMessagebox(title="Updating Segy file", icon="check.png",
                  message="Saved Header into Segy File")
     text.delete("1.0", tk.END)

   else:
     show_error()

def clean():
    text.delete("1.0", tk.END)


def scrapebinary():
   binheader = segy_bin_scrape(filesegy)
   
   clean()
   for key, value in binheader.items():
     #print(f"{key}: {value}")
    text.insert(tk.END, str(f"{key}: {value}") + '\n')


text = tk.Text(root, wrap="word", undo=True)
text.pack(expand="yes", fill="both")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="EBCDIC", menu=file_menu)
file_menu.add_command(label="Extract EBCDIC from segy file", command=open_segy)
file_menu.add_command(label="Read EBCDIC from a file", command=open_file)
file_menu.add_command(label="Save EBCDIC header into a file", command=save_file)
file_menu.add_command(label="Update EBCDIC in cuurent segy", command=save_segy)
file_menu.add_separator()
file_menu.add_command(label="Clear pad", command=clean)
file_menu.add_command(label="Exit", command=root.destroy)


file_menu1 = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="BINARY HEADER", menu=file_menu1)
file_menu1.add_command(label="Extract Binary from segy file", command=scrapebinary)
#file_menu1.add_command(label="List Header values", command=binlist)
file_menu1.add_separator()
file_menu1.add_command(label="Clear pad", command=clean)
#file_menu1.add_command(label="Open", command=open_file)
#file_menu1.add_command(label="Save", command=save_file)


root.mainloop()
