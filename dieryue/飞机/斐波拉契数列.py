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

    
