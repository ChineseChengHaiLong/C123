class Zidan:
    def __init__(self,name,shanghai):
        self.name=name
        self.shanghai=shanghai
       
    def __str__(self): 
        s='当前子弹的名字是穿甲弹是'+self.name+',击中一颗的伤害是'+self.shanghai
        return s
class Danjia:
    def __init__(runliang,tanchu):
        self.cunliang=runliang
    def __str__(self):
        d='弹夹的容量为：'+self.runliang
        return d
    def sheng_yu(self):
        shengyu=rongliang-tanchu
        print('击中%d，目前弹夹还有%d颗'%(self.tanchu,shengyu))
class Qing:
    def __init__(self,andno,jiazidan):
        self.andno=andno
    def __str__(self):
        xian = 0
        xian=xian+self.jiazidan
        s=print('加了%d颗子弹,现在弹夹里的子弹个数为:%d' % (self.jiazidan,xian))
        return s
class People:
    def __init__(self,name,height,weight):
        
        self.name=name
        self.height=height
        self.weight=weight
    def na_qiang(self):
        print('老王看到了歹徒在行凶')
        print('老王拿起了枪')
    def cha_dan(self):
        print('查看弹夹')
    def shang_tang(self):
        print('把枪上膛，瞄准歹徒，准备开枪')
    def sheji(self):
        print('啪啪啪啪啪。。老王开枪射击')
    def dai_tu(self,xueliang,zhong):
        print('歹徒的血量是%d'% self.xueliang)
        diao=zhong*10
        shengo=xueliang-diao
        if zhong < 0:
            print('你在开玩笑吗，没子弹怎么玩，走了')
        elif zhong > 0 and zhong < 5:
            print('歹徒中弹%d颗,损失了%d的血,还剩下%d的血,他向敌战区跑去'% (self.zhong,diao,shengo))
        else:
            print('歹徒已经被老王击毙')
    def __str__(self):
        return '姓名:'+self.name+',身高:'+self.height+'米,体重'+self.weight
laowang=People('老王','2','160')
print(laowang)
laowang.na_qiang()
