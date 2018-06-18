class People(object):
    guoji='china'
    
    name='小明'
    @classmethod
    def get_name(sel):
        return sel.name
    @classmethod
    def aa (cls):
        return cls.guoji
people=People()
print(people.guoji)
print(People.guoji)
print(people.get_name())
print(People.get_name())
print(people.aa())
print(People.aa())
print(people.name)
print(People.name)


class Tools(object):
    @staticmethod
    def dao():
        print('*'*10)
        print('1、上上签')
        print('1、桃花')
    def bao(s):
        Tools.dao()
        print(s,'天王盖娣胡')
Tools.bao('小鸡吨毛孤')
