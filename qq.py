from random import randint
n=randint(900,1300)
print('生成随机数为%d' %n)
i=600
while True:
    num=int(input('崔康的真实体重来证明他是猪:'))
    i+=100
    if(num>n):
        print('对正确，崔康是猪干哈!')
    elif(num<n):
        print('错误，太小了都说了他是猪!')
else :
        print('回答正确,他就是猪')
