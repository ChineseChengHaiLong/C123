import random
a=6
while  1<a:
    x = random.randint(1,7)
    y = random.randint(1,5)
    print("横排的是 %d ,竖排的是 %d " % (x,y))
    print("&"*50)
    a=a-1
