from tkinter import *
import os
import tkinter.filedialog
import ppt2pdf
from ppt2pdf import PDFConverter
from rename import rename
root = Tk()
root.title('Speed')
root.geometry('600x600')
directory = os.path.abspath('.')


def xz():
    # filename = tkinter.filedialog.askopenfilename()
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        lb.config(text="您选择的文件是："+filename)
        globals()["directory"] = filename

    else:
        lb.config(text="您没有选择任何文件")


def xxtopdf():
    if directory != "":
        pdfConverter = PDFConverter(directory)
        pdfConverter.run_conver()


def rename_com():
    rename(directory, e_rename.get())

#选择文件
lb = Label(root, text=os.path.abspath('.'))
lb.grid(row=0, column=1, sticky=E+W)
btn_choose_file = Button(root, text="选择需要处理的文件夹", command=xz)
btn_choose_file.grid(row=1, column=1, sticky=E+W)

#选择文件夹转为pdf
btn_xxtopdf = Button(root, text="选择文件转为pdf", command=xxtopdf)
btn_xxtopdf.grid(row=2, column=1, sticky=E+W)

#选择文件夹将里面文件重命名
l_rename = Label(root, text='文件主体名:')
l_rename.grid(row=3, column=0, sticky=E+W)
e_rename = Entry(root)
e_rename.grid(row=3, column=1, sticky=E+W)
btn_rename = Button(root, text="命名文件", command=rename_com)
btn_rename.grid(row=4, column=1, sticky=E+W)

root.mainloop()
