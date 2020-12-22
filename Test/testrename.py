import sys
import os
sys.path.append(os.path.split(sys.path[0])[0])
from fun.rename import rename

def testRename(directory,directory_new,new_name):
    flag = 1
    rename(directory, new_name)
    f1 = os.listdir(directory)
    f2 = os.listdir(directory_new)
    if (len(f1)-1) != len(f2):
        print("The num is incommon!")
        flag=0
    for filename in f2:
        if filename.find(new_name) == -1:
            print("The name is incorrect!")
            flag=0
            break
    for filename in f2:
        os.remove(os.path.join(directory_new,filename))
    os.rmdir(directory_new)
    if flag:
        print("Success!")

if __name__ == '__main__':
    directory = "./TestData/Rename/"
    directory_new = directory+"new/"
    new_name = "Rename"
    testRename(directory,directory_new,new_name)