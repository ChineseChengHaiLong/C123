while True:
    import random
    people=int(input("请输入1-3数字来跟机器人玩一把紧张刺激的剪刀石头布的游戏 1*剪刀,2*石头,3*布:"))    
    pc = random.randint(1, 3)
    if pc == 1:
        print("电脑输出的是:剪刀")
    elif pc == 2:
        print("电脑输出的是:石头")
    else:
        print("电脑输出的是:布")
    if people == 1:
        print("哥您输出的是:剪刀")
    elif people == 2:
        print("哥您输出的是:石头")
    else:
        print("哥您输出的是:布") 
    if people >= 1 and people <= 3: 
        if (people == 1 and pc == 3) or (people == 2 and pc == 1) or (people == 3 and pc == 2):
            print("good win")
        elif people == pc:
            print("平局")
        else:
            print("lose")
    else:
        print("见鬼去吧，不认识1-3之外的数字?")
    print("&"*49)                                             
