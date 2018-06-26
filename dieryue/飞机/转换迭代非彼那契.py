'''
def day(shu):
    n =  0
    a = 0
    b = 1
    while n < shu:
        yield (b)
        a,b = b, a+b
        n += 1
    return 'OK'
g=day(10)
print(next(g))
print(next(g))

Q = [x for x in range(1,101)]
W = []
Q=iter(Q)
a = 0
b = 1 
while True:
    W.append.(b)
    a,b = b, a+b
    for i in L:
        if b < i:
    print(b)
'''    

L = [x for x in range(100)]
P = []
L = iter(L)
n =0
a =0
b =1
while n < 100:
    P.append(b)
    a,b = b,a+b
    n += 1
for i in L:
    if i in P:
        print(i)
