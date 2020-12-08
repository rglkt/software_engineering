import os
def rename(directory,name):
    # name=input('地名:')
    # print('\n')
    # directory=input('请输入文件路径(结尾加上/)：')       
    #获取该目录下所有文件，存入列表中
    f=os.listdir(directory)
    n=0
    for i in f:
        #设置旧文件名（就是路径+文件名）
        oldname=directory+'/'+f[n]
        #设置新文件名
        newname=directory+'/'+name+str(n+1)+'.'+f[n].split('.')[-1]
        #用os模块中的rename方法对文件改名
        os.rename(oldname,newname)
        print(oldname,'======>',newname)
        n+=1