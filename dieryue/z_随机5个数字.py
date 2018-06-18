import random
list1=[]
a=0
while a < 5:
    a=a+1
    pc=random.randint(1,10)
    list1.append(pc)
    if list1.count(pc)>1:
        a=a-1
        list1.pop()
for i in list1:
    print(i)
    
