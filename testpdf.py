import os

import ppt2pdf
from ppt2pdf import PDFConverter

directory = "E:/test/PPT"


if directory != "":
    pdfConverter = PDFConverter(directory)
    pdfConverter.run_conver()

def reportdiff(unique1, unique2, dir1, dir2):
    '''
    生成目录差异化报告
    '''
    if not (unique1 or unique2):
        print("Directory lists are identical")
    else:
        if unique1:
            print('Files unique to：', dir1)
            for file in unique1:
                print(file)
        if unique2:
            print('Files unique to：', dir2)
            for file in unique2:
                print(file)


def difference(seq1, seq2):
    '''
    仅返回seq1中的所有项
    '''
    return [item for item in seq1 if item not in seq2]


def comparedirs(dir1, dir2, files1=None, files2=None):
    '''
    比较文件的名字
    '''
    print('Comparing...', dir1, 'to....', dir2)
    files1 = os.listdir(dir1) if files1 is None else files1
    files2 = os.listdir(dir2) if files2 is None else files2
    unique1 = difference(files1, files2)
    unique2 = difference(files2, files1)
    reportdiff(unique1, unique2, dir1, dir2)
    return not (unique1, unique2)



if __name__ == '__main__':
    dir1 = "E:/test/PPT"
    dir2 = "E:/test/PPT/pdfconver"
    comparedirs(dir1, dir2)
