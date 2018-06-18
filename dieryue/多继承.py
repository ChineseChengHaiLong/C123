class lv(object):
    def man(self):
        print('姓驴走的特慢')
    def jiao(self):
        print('咕咕叫。。。')
class ma(object):
    def kuai(self):
        print('姓马耐力超强')
    def jiao(self):
        print('嗷嗷嗷嗷嗷嗷叫....')
class luozi(lv,ma):
    def eat(self):
        print('吃得还挺多')
    def jiao(self):
        print('莽莽莽叫')
luo=luozi()
luo.man()
luo.kuai()
luo.eat()
luo.jiao()
print(luozi.__mro__)  
class Father(object): 
    def __init__(self,name):
        self.xing=name
    def kaiche(self):
        print('是个老四机')
    def eat(self):
        print('特能吃')
class Son(Father):
    def __init__(self,name):
       # self.ming=name
        #Father.__init__(self.name)
        #super(son.self).__init__(name)
        super().__init__(name)
    def kaiche(self):
        super().kaiche()
        print('还是个赛车收')
son=Son('大头儿子')
print(son.xing)
son.kaiche()
