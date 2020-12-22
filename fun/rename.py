import os
import shutil
def rename(directory,name):
    f=os.listdir(directory)
    if not os.path.exists(directory+'/new/'):
        os.mkdir(directory+'/new/')
    n=0
    for i in f:
        oldname=directory+'/'+f[n]
        newname=directory+'/new/'+name+str(n+1)+'.'+f[n].split('.')[-1]
        shutil.copyfile(oldname,newname)
        # os.rename(oldname,newname)
        print(oldname,'======>',newname)
        n+=1