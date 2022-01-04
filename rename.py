# rename files in a folder as <provided prefix><num>.<original extension>
# num starts from 0

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory, askopenfilename
import re
import os


window = Tk()
window.title('Batch Rename')
window.geometry('500x400')
window.resizable(width=False, height=False)

intro_text = '''
Rename files in selected folder to form <prefix><num>.<extension>
If no prefix provided, file would be named <num>.<extension>
Default num starts from 0
'''

intro_demo = '''
Example: 
/Desktop/graduation2021
|-- graduation0.png  
|-- graduation1.png
|-- ...
'''
label_intro = Label(window, text=intro_text)
label_intro.place(x=20, y=10)
label_demo = Label(window, text=intro_demo, justify=LEFT)
label_demo.place(x=20, y=80)

def select_folder():
    input_folder = askdirectory(title='Select folder')
    path_folder.set(input_folder)

path_folder = StringVar()
entry_folder = Entry(window, width=30, textvariable=path_folder)
entry_folder.place(x=20, y=200)
button_folder = Button(window, text='Select folder', command=select_folder, width=18, height=1)
button_folder.place(x=300, y=200)

findBathroom= re.compile(r'<p class="rentInfoDetail">(.*) ba</p>')


prefix_re = re.compile(r'[a-zA-Z0-9_]+')
def set_prefix():
    if len(prefix.get()) == 0:
        prefix.set(None)
    elif len(re.findall(prefix_re, prefix.get())) == 0:
        messagebox.showerror(title='prefix naming error', message='prefix can only contain contain letters, numbers, and/or underscores')

prefix = StringVar()
entry_prefix = Entry(window, width=30, textvariable=prefix)
entry_prefix.place(x=20, y=230)
button_prefix = Button(window, text='Enter prefix', command=set_prefix, width=18, height=1)
button_prefix.place(x=300, y=230)


def rename_files():
    dir = path_folder.get()
    pre = prefix.get()
    files = os.listdir(dir)
    i = 0
    for f in files:
        ext = os.path.splitext(f)[1]
        if pre is None:
            newname = str(i) + ext
        else:
            newname = pre + str(i) + ext
        os.rename(dir+'/'+f, dir+'/'+newname)
        i += 1
    print('Successfully renamed all files in folder')
button_rename = Button(window, text='Rename files', command=rename_files, width=18, height=1)
button_rename.place(x=150, y=260)


window.mainloop()

