class Barbecue:
    def __init__(self):
        self.into='在水中的鱼'#定义鱼的初始状态
        self.time1=0#定义初始烘烤时间
        self.seasoning=[]#以列表形式定义初始要添加的佐料
    def __str__(self):#返回烘烤鱼的状态或流程
        name =''
        for i in self.seasoning:#遍历佐料这个列表
            name =name+i + ','
        name=name.strip(',')
        p=  (' 烤鱼的状态为:%s ,烤的时间是:%d分钟 ,添加的调料有:%s' % (self.into,self.time1,name))
        return p
    def shijian(self,time2):
        self.time1=self.time1+time2
        if self.time1 >0 and self.time1 < 4:
             self.into='刚抓的鱼'
        elif self.time1 >= 4 and self.time1 <= 6:
            self.into='新鲜的鱼'
        elif self.time1 > 6 and self.time1 <=8:
            self.into='半熟的鱼'
        elif self.time1 > 8 and self.time1 <=10:
            self.into='烤刚刚好，多滋多味'
        elif self.time1 > 10:
            self.into='糊了，都黑了'
    def zhuijia(self,jia):

        self.seasoning.append(jia)

while True:
    time2=int(input('请输入您要烤置的时间：'))
    jia=input('请输入您要添加的调料:')
    tiao = Barbecue()
    print(tiao.into)
    tiao.shijian(time2)
    print(tiao.into)
    tiao.zhuijia(jia)
    print(tiao)








