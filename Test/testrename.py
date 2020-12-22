import sys
import os
sys.path.append(os.path.split(sys.path[0])[0])
from fun.rename import rename
if __name__ == '__main__':
    directory = "./TestData/Rename/"
    directory_new = directory+"new/"
    new_name = "Rename"
    rename(directory, new_name)
    f1 = os.listdir(directory)
    f2 = os.listdir(directory_new)
    if (len(f1)-1) != len(f2):
        print("The num is incommon!")
    for filename in f2:
        if filename.find(new_name) == -1:
            print("The name is incorrect!")
            break
    for filename in f2:
        os.remove(os.path.join(directory_new,filename))
    os.rmdir(directory_new)