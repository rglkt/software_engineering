from tkinter import *
import os
import tkinter.filedialog
import ppt2pdf
from ppt2pdf import PDFConverter
root = Tk()
root.title('批量处理文件软件')
root.geometry('300x100')
directory = ""


def xz():
    # filename = tkinter.filedialog.askopenfilename()
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        lb.config(text="您选择的文件是："+filename)
        globals()["directory"]= filename
         
    else:
        lb.config(text="您没有选择任何文件")

def xxtopdf():
    if directory!="":
            pdfConverter = PDFConverter(directory)
            pdfConverter.run_conver()

lb = Label(root, text='')
lb.pack()
btn_choose_file = Button(root, text="选择需要处理的文件夹", command=xz)
btn_choose_file.pack()
btn_xxtopdf = Button(root,text="选择文件转为pdf",command = xxtopdf)
btn_xxtopdf.pack()

root.mainloop()
