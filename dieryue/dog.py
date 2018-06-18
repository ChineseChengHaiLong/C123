class Animal:
     def __init__(self,name):
         self.name=name
     def set_name(self): 
         f=open('name.txt','w') 
         f.write(self.name)
         f.close()
         f=open('name.txt','r')
         s=f.read()
         f.close()
         if len(s) != 0:
             return self.name
         else:
             return '请新建内容'
       
     def __del__(self):
         print('已删除*****************')
     
             
dog=Animal('大`黄')
g=dog.set_name()
print(g)
dog1=dog
dog2=dog
del dog
print('==============')

