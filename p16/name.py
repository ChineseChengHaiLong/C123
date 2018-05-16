'''
name_list=[] 
while True:
    user = input("请输入大家的名字：") 
    name_list.append(user)
    if user == 'q':
        break 
print("列表中第3位是：%s" % name_list[3] )
print("列表中第5位是：%s" % name_list[5]  )
print("列表中第8位是：%s" % name_list[8]  )
print("列表中第10位是：%s" % name_list[10]  )
name_list.sort()
print
'''

user_list=[]
while True:
    user=input("请输入大家的名字：")
    user_list.append(user)
    if user == 'q':
        break
print("列表中下标是3的同学是: %s " % user_list[3])
print("列表中下标是5的同学是: %s " % user_list[5])
print("列表中下标是8的同学是: %s " % user_list[8])
print("列表中下标是10的同学是: %s " % user_list[10])
user_list.sort()
print(user_list)
user_list.sort(reverse=True)
print(user_list)
user_list.pop
print(user_list)
user_list.pop(8)
print(user_list)
dier_list=[1,2,3,4,5,6,7,'fds','sf','fsf','sf','ss','ff']
user_list.extend(dier_list)
print(user_list)
w = user_list.index("小明")
print(w)


  
