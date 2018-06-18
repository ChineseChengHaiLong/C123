def jia (a,b):
    return a+b
def jian (a,b):
    return a-b
def cheng(a,b):
    return a*b
def chu(a,b):
    return a/b
aa=float(input('请输入第一个数字:'))
while True:
    bb=input('请输入要记算得方式:')
    cc=float(input('请输入另一个数字:'))
    if bb == '+':
        dd=jia(aa,cc)
        print(dd)
    elif bb == '-':
        dd=jian(aa,cc)
        print(dd)
    elif bb =='*':
        dd=cheng(aa,cc)
        print(dd)
    elif bb == '/':
        dd=chu(aa,cc)
        print(dd)
    aa=dd
