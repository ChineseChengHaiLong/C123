class QUanhuang:
    def __init__ (self,name,age,sex,weight,faxing):
        self.name=name
        self.age=age
        self.sex=sex
        self.weight=weight
        self.faxing=faxing
    def __str__(self):
        jieshao ='<**-**>出场人物是'+self.name+'\t年龄:'+self.age+'\t性别'+self.sex+'\t重量'+self.weight+'\t发型'+self.faxing
        return jieshao
        
    def jump(self):
        print('红丸跳了一下，刚好跳到小金刚的脚上')
    def da(self):
        print('%s看到有个二哈跳到自己的脚上使出一招天残脚，嗖嗖嗖....' % self.name)
    def fei(self):
        print('红丸飞了，飞得好远，掉下来了。')
        print('嗖嗖嗖嗖,使出了一招失传已久从天而将的掌法如来神掌')
    def ti(self):
        print('%s又使出蛤蟆功，体外凝聚出了蟾蜍的真气外衣，' % self.name)
        print('一道冲天的光芒扑向对手,两道能量相撞，漫天的灰尘遮蔽了天空')
        print('随既两道身影从茫茫尘埃中冲天而起，又战在一起')
    def hunzhan(self):
        print('%s加入了战斗，如一头野猪凶狠很的拱向白菜，三人就此打的难舍难分，             打得天蹦地裂，日月无光，看似战斗马上要分出了结果。' %self.name)
    def sile(self):
        print('分出结果了，红丸落败了，从此再也没有了红丸的辉煌')
    def hunzhan1(self):
        print('%s坐享鱼翁之力，加入战斗' % self.name)
    def huanzhan2(self):
        print('谁知螳螂捕禅黄雀在后，%s也加入了战斗' % self.name)
    def shengli(self):
        print('经过难舍难分的战斗，胜利者呈现在世人的眼前，那就是来自我大华夏的葫芦小金刚')
hongwan=QUanhuang('红丸','30','男','150','平头')
print('%s先出场了，发行清新亮丽一头%s' % (hongwan.name,hongwan.faxing))
print(hongwan)
huaxia=QUanhuang('葫芦小金刚','20','男','140','冲天辨')
print(huaxia)
huaxia.jump()
huaxia.da()
huaxia.fei()
huaxia.ti()

mali=QUanhuang('玛丽','34','女','100','烫头')
mali.hunzhan()
mali.sile()

andi=QUanhuang('安迪','21','男','200','刺头')
andi.hunzhan1()
damen=QUanhuang('大门','30','男','199','光头')
damen.huanzhan2()
damen.shengli()

