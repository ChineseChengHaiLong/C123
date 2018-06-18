class Student:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
        self.grade={}
    def zuijia(self,keys,values):
        self.grade[keys]=values
    def __str__(self):
        return'姓名'+self.name+'性别'+self.sex+'年纪'+self.age+'成绩'+str(self.grade)
def hanshu(a):
    for i in range(1,6):
        keys = input('请输入科目')
        values= input('请输入成绩')
        a.zuijia(keys,values)
def da_yin():
    f=open('dayin.txt','a')
    f.write(print(xiaoming))
    f.write(print(xiaoxiao))
    f.write(print(xiaohua))
xiaoming=Student('小明','男','13')
hanshu(xiaoming)
print(xiaoming)
xiaohua=Student('小花','女','12')
print(xiaohua)
xiaoxiao=Student('小小','女','15')
print(xiaoxiao)
da_yin()
