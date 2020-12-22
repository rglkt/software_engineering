from tkinter import *
import os
import tkinter.filedialog
import fun.ppt2pdf
from fun.ppt2pdf import PDFConverter
from fun.rename import rename
from fun.mergeExcel import mergeExcel
root = Tk()
root.title('Speed')
root.geometry('600x600')
directory = os.path.abspath('.')

def xz():
    # filename = tkinter.filedialog.askopenfilename()
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        lb.config(text="The file you have selected is:"+filename)
        globals()["directory"] = filename

    else:
        lb.config(text="You did not select any files")

def xxtopdf():
    if directory != "":
        pdfConverter = PDFConverter(directory)
        pdfConverter.run_conver()

def rename_com():
    rename(directory, e_rename.get())

def mergeExcel_but():
    mergeExcel(path=directory)

layout_row = 0
# 选择文件
lb = Label(root, text=os.path.abspath('.'))
lb.grid(row=layout_row, column=1, sticky=E+W)

layout_row += 1
btn_choose_file = Button(
    root, text="Select the folder that you want to process", command=xz)
btn_choose_file.grid(row=layout_row, column=1, sticky=E+W)

# 选择文件夹转为pdf
layout_row += 1
l_pdf = Label(root, text='Batch files in the folder to PDF')
l_pdf.grid(row=layout_row, column=1, sticky=E+W)
layout_row += 1
btn_xxtopdf = Button(root, text="convert to pdf", command=xxtopdf)
btn_xxtopdf.grid(row=layout_row, column=1, sticky=E+W)

# 选择文件夹将里面文件重命名
layout_row += 1
l_file = Label(root, text='Rename the files in the folder by batch')
l_file.grid(row=layout_row, column=1, sticky=E+W)
layout_row += 1
l_rename = Label(root, text='File body name:')
l_rename.grid(row=layout_row, column=0, sticky=E+W)
e_rename = Entry(root)
e_rename.grid(row=layout_row, column=1, sticky=E+W)
layout_row += 1
btn_rename = Button(root, text="rename file", command=rename_com)
btn_rename.grid(row=layout_row, column=1, sticky=E+W)


# 合并excel表格
layout_row += 1
l_excel_merge = Label(root, text='Merge Excel tables')
l_excel_merge.grid(row=layout_row, column=1, sticky=E+W)
layout_row += 1
l_excel_row = Label(root, text='From which row:')
l_excel_row.grid(row=layout_row, column=0, sticky=E+W)
e_excel_row = Entry(root)
e_excel_row.grid(row=layout_row, column=1, sticky=E+W)
layout_row += 1
l_excel_col = Label(root, text='From which column:')
l_excel_col.grid(row=layout_row, column=0, sticky=E+W)
e_excel_col = Entry(root)
e_excel_col.grid(row=layout_row, column=1, sticky=E+W)

layout_row += 1
btn_excel_merge = Button(root, text="Merge Excel tables", command=mergeExcel_but)
btn_excel_merge.grid(row=layout_row, column=1, sticky=E+W)

root.mainloop()