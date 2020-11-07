from tkinter import *
import tkinter.filedialog

root = Tk()
root.title('批量处理文件软件')
root.geometry('300x100')
directory = ""
def xz():
    # filename = tkinter.filedialog.askopenfilename()
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        lb.config(text = "您选择的文件是："+filename);
    else:
        lb.config(text = "您没有选择任何文件");

lb = Label(root,text = '')
lb.pack()
btn_choose = Button(root,text="选择需要处理的文件夹",command=xz)
btn_choose.pack()




root.mainloop()