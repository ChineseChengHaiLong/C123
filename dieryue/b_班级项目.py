class Banji:
    def __init__(self,teacher,number):
        self.teacher=teacher
        self.number=number
        self.student=[]
        self.student1=[]
    def zhui(self):
        self.student.append(self.teacher)
        self.student.append(self.number)
    def __str__(self):
        return '班主任是:'+self.teacher+'班级编号是:'+self.number
class Student:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex
        self.grade={}
    def zhuijia(self):
        self.grade['姓名']=self.name
        self.grade['年龄']=self.age
        self.grade['性别']=self.sex
        
    def __str__(self):
        return '姓名是:'+self.name+'年龄是:'+self.age+'性别是:'+self.sex
        
        
class Grade:
    def __init__(self,yuwen,shuxue,english):
        self.yuwen=yuwen
        self.shuxue=shuxue
        self.english=english
        self.chengji={}
        
    def get_cha(self,people):
        if people == '语文':
            s =  return self.yuwen
            print(s)
        elif people == '数学':
            return self.shuxue
        elif people == '英语':
            return self.english
        else :
            return '见鬼，这门科目没有开始'
    def set_cha(self.cha,gai):
        if cha == '语文':
            return self.gai
        elif cha == '数学':
            return self.gai
        elif cha == '英语':
            return self.gai
    def ke(self):
        self.chengji['语文']=self.yuwen
        self.chengji['数学']=self.shuxue
        self.chengji['英语']=self.english
    def __str__(self):
        return '语文成绩是:'+self.yuwen+'数学成绩是:'+self.shuxue+'英语成绩是:'+self.english
def xinjian():
    a=0
    while True:
        a=a+1
        if banji1 ==  'q':
            print('已退出')
            break
        banji1=input('请输入班主任的名字:')
        bianhao=input('请输入班级的编号:')
        bian=Banji(banji1,bianhao)
        bian.zhui()
        print(bian)
        name1=input('请输入第%d个学生的名字:' % a)
        age1=input('请输入年龄:')
        sex1=input('请输入性别:')
        xiaoming=Student(name1,age1,sex1)
        xiaoming.zhuijia()
        print(xiaoming)
        yuwen1=input('请输入语文成绩:')
        shuxue1=input('请输入数学成绩:')
        english1=input('请输入英语成绩:')
        chengji1=Grade(yuwen1,shuxue1,english1)
        chengji1.ke()
        print(chengji1)
        chengji1.chengji.update(xiaoming.grade)
        chengji1.chengji['编号']=str(a)
        bian.student.append(chengji1.chengji)#把班级的详细信息都追加到初始的列表中
        
        
        
            


