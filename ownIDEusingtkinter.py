from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
from tkinter.messagebox import showinfo
import subprocess

compiler=Tk()
compiler.title("My PYcharm+VScode")
file_path=''

def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path=='':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])

    else:
        path=file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path == '':
        save_prompt=Toplevel()
        text=Label(save_prompt,text="please save your code")
        text.pack()
        return
    command=f'python {file_path}'
    process=subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output , error = process.communicate()
    code_output.insert(1.0,output)






def cut():
    editor.event_generate(("<<Cut>>"))

def copy():
    editor.event_generate(("<<Copy>>"))

def paste():
    editor.event_generate("<<Paste>>")

def About():
    showinfo("This is a simple IDE made by sharik ")



menu_bar=Menu(compiler)

file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label='open', command=open_file)
file_menu.add_command(label='save as', command=save_as)
file_menu.add_command(label='save', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File',menu=file_menu)

run_bar=Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run',menu=run_bar)

edit_menu=Menu(menu_bar,tearoff=0)
edit_menu.add_command(label='cut', command=cut)
edit_menu.add_command(label='copy', command=copy)
edit_menu.add_command(label='paste', command=paste)
menu_bar.add_cascade(label='Edit',menu=edit_menu)

About_menu=Menu(menu_bar,tearoff=0)
About_menu.add_command(label='about', command=About)
menu_bar.add_cascade(label='About',menu=About_menu)


compiler.config(menu=menu_bar)



editor=Text()
editor.pack()

code_output=Text(height=10)
code_output.pack()


compiler.mainloop()
