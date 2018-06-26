L = [x for x in range(1,101)  if x%2 != 0]
for i in L:
    print (i)


def jishu(aa):
    n = 1
    while n < aa:
        if n%2 != 0:
            yield n
        n += 1
    
aa = int(input('请输入从1 到 几的奇数'))
P = jishu(aa)
for i in P:
    print(i)
#L = [i for i in range(1,101) for x in range(2,i) if x%x == 0 and x%1 == 0] 
#for i in L:
 #   print(i)
