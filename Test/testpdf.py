import sys
import os
sys.path.append(os.path.split(sys.path[0])[0])
import fun.ppt2pdf
from fun.ppt2pdf import PDFConverter

def comparedirs(dir_org,dir_pdf):
    org = os.listdir(dir_org)
    pdf = os.listdir(dir_pdf)
    flag = 1
    for pdf_file in pdf:
        if pdf_file.split('.')[-1].lower() != 'pdf':
            print("File's type error!")
            flag=0
            break
    for org_name in org:
        if org_name.split('.')[0]+'.pdf' not in pdf and org_name!='pdfconver':
            print("File's name error or file's number error!")
            flag=0
            break
    if flag:
        print("Success!")

if __name__ == '__main__':
    dir1 = "./TestData/PPT/"
    dir1 = os.path.abspath(dir1)
    dir2 = "./TestData/PPT/pdfconver"
    dir2 = os.path.abspath(dir2)
    if dir1 != "":
        pdfConverter = PDFConverter(dir1)
        pdfConverter.run_conver()
    comparedirs(dir1, dir2)
    f = os.listdir(dir2)
    for file in f:
        os.remove(os.path.join(dir2,file))
    os.rmdir(dir2)