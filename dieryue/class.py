class chelei:
    def __str__(self):
        s='车的名字'+self.name+'车的重量是'+self.size+'车的颜色是'+self.color+'车的类型是'+self.type1
        return s
    def __init__(self,name,size,color,type1):
        self.name=name
        self.size=size
        self.color=color
        self.type1=type1
    def jiuyuan(self):
        print('%s联合国爱心救援'% self.name)
        print('%s退休之后，开启了自驾车好不自在' % self.name)
    def zhanzheng(self):
        print('%s保家为国，守护边疆' % self.name)
        print('%s退役之后,跑起了公交车'% self.name)
    def yunshu(self):
        print('%s公交司机很辛苦'% self.name)
    def jiaoche(self):
        print('%s自驾游观光'% self.name) 
    def jieshao(self):
        print('我开的是%s, 重量为%s吨, 颜色为%s, 类型为%s ' % (self.name,self.size,self.color,self.type1))
tanke = chelei('坦克','40','黑色','作战')
tanke.jieshao()
tanke.zhanzheng()
print(tanke)
jiuyuanche = chelei('救援车','30','白色','救援')
jiuyuanche.jieshao()
jiuyuanche.jiuyuan()
gongjiao = chelei('公交车','20','蓝色','拉客')
gongjiao.jieshao()
gongjiao.yunshu()
xiaoche = chelei('轿车','10','黑色','自驾游')
xiaoche.jieshao()
xiaoche.jiaoche()
