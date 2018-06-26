def test(a):
    def test_in(b):
        print('里面的内容是:%d' % b)
        return b+a
    return test_in
f = test(5)(10)
print(f)
