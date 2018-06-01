f=open('a.txt','w')
f.write('大漠孤烟直\n长河落日远\n欲穹千里暮\n更上一层楼\n')
f.close()
f=open('a.txt','r')
a=f.readlines()
f.close()
f=open('a.txt','w')
for i in a:
    print(i[0:-1]+'*-*')
f.close()

'''
f = open('a.txt', 'r')
a = f.readline()
print("1:%s"%a)
a = f.readline()
print("2:%s"%a)
f.close()
'''
print('文件名子是：',f.name)
print('文件是否关闭：',f.closed)
print('文件的打开模式是:',f.mode)
