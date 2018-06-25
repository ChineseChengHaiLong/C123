class People(object):
    def __init__(self):
        self.__money = 50
    def get_a(self):
        self.__money = 500 
        return self.__money
    def set_a(self,value):
        self.__money = value
    qian = property(get_a,set_a)
huahua = People()
ll=huahua.get_a()
print(ll)
huahua.money = 99999999999
print(huahua.money)

class People(object): 
    def __init__(self):
        self.__money = 1
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,value):
        self.__money = value
p = People()
print(p.money)
p.money = 888888
print(p.money)

