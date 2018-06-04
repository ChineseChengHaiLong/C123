def homename(h):#定义一个函数
    f=open(h,'r')#打开输入的文件
    p=h.rfind('.')#查找‘.’的下标是多少
    p1=h[:p]#取‘.’前面的内容
    p2=h[p:]
    print(p1)
    print(p2)
    a=open(p1+'副本'+p2,'w')#打开一个新建的文件
    while True:
       size = f.read(1024)
       if len(size) == 0:
           break
       a.write(size)#把源文件的内容复制到新文件里面
    f.close()#关闭源文件
    a.close()#关闭新文件
    
t=input('请输入您要复制的的文件名称：')
homename(t)
