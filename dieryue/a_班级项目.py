class Banji:
    def __init__(self,teacher,number):
        self.teacher=teacher
        self.number=number
        self.student=[]
        self.student1=[]
        self.student2=[]
        self.grade={}
    def add_a(self):
        self.student1.append(self.teacher)
        self.student1.append(self.number)
        self.student1.append(self.grade)
        self.student2.extend(self.student1)
    def __str__(self):
        for i in self.student1:
           s= print(i)
        return s
        
class Student(Banji):
    def __init__(name,age,sex):
        self.name=name
        self.age=age
        self.sex
           
    def add_ji(self,keys,values):
        for i in range(1,4):
            keys=input('请输入课程')
            values=input('请输入成绩') 
            self.grade[keys]=values
            self.student.append(self.grade)
    def cha_vun(self):
        for i in self.student:
            print('姓名:%s\n年龄:%s\n性别:%s\n成绩:%s' % (self.name,self.age,self.sex,str(self.grade)))     
class Grade(Student):
    def __init__(yuwen,shuxue,english):
        self.yuwen=yuwen
        self.shuxue=sshuxue
        self.english=english 
       
        
    def get_cha(self,people):
        if people == '语文':
            return self.yuwen
        elif peoplr == '数学':
            return self.shuxue
        elif people == '英语':
            return self.english
        else:
            return '没这个科目，明年再来把，拜拜'
    def __str__(self):        
        return '语文:'+self.name+'数学'+self.shuxue+'英语'+self.english
teacher=input('请输入班主任名字')
number=input('请输入班级编号')
xiaoming=Banji(teacher,number) 
print(xiaoming)               
