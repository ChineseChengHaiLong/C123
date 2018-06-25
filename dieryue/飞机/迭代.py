
'''
L = [x*2 for x in range(1,8)]
print(L)
L = (x*2 for x in range(1,8))
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))
for i in L:
    print(i)
'''
from inspect import isgeneratorfunction
def Father(a,b):
    while a < b:
        yield a
        a += 1
c=Father(2,10)

print(next(c))
print(isgeneratorfunction(Father))
