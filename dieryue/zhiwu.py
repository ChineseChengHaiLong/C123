
class Xrk:
    def __init__(self,name,yanse,shuliang,hp):
        self.name=name
        self.yanse=yanse
        self.shuliang=shuliang
        self.hp=hp
    def faguang(self):
        print('%s发出耀眼的光芒，收获颇丰' % self.name)
        print('有钱的感觉真好又可以种植其他的作战植物了')
    def shouhuo(self):
        print('%s一次收获五十个金币'%self.name)
    def dongzuo(self):
        print('%s洋溢着欢快的笑。随风缪动着身姿'% self.name )
    def __str__(self):
        s=self.name+'缓慢的出来了，天啊转眼就长大了,'+'很闪眼睛,散发出'+self.yanse+self.shuliang+'棵很多很多'+self.hp+'的血量满满，向你挑逗'
        return s
yihao=Xrk('向日葵','金色','10','100')
print(yihao)
yihao.dongzuo()
yihao.shouhuo()
yihao.faguang()
class wandou:
    def __init__(self,name,yanse,hp,lihai,shuliang):
        self.name=name
        self.yanse=yanse
        self.hp=hp
        self.lihai=lihai
        self.shuliang=shuliang
    def __str__(self):
        d=self.name+'冒出了头，猥琐全场,'+self.yanse+'的发亮,'+'血量'+self.hp+',攻击力'+self.lihai+',炮弹数量'+self.shuliang
        return d
    def gongji(self):
        print('僵尸出现了，一大波怎么办,边打边支援')
        print('%s把炮口对准僵尸出现的方向'% self.name )
        print('放他们靠近再打，随时准备进攻.....')
        print('进攻，发豌豆让他们吃，撑死他们...')
    def yaotou(self):
        print('摇头,眼睛犀利而深邃，在狂风中晃起了脑袋')
    def si(self):
        print('不行太多了，快要被吃掉了,赶快装死，啊 我死了。。')
douyi=wandou('绿豌豆','绿','100','200','50')
douyi1=wandou('绿豌豆','绿','100','200','50')
print(douyi)
douyi.yaotou()
douyi.gongji()
douyi.si()
print(douyi1)
douyi.yaotou()
douyi.gongji()
douyi.si()
class dilei:
    def __init__(self,name,yanse,hp,lihai,shuliang):
        self.name=name
        self.yanse=yanse
        self.hp=hp
        self.lihai=lihai
        self.shuliang=shuliang
    def __str__(self):
        p=self.name+'偷偷冒出了头，猥琐全场,'+self.yanse+'的吓人,'+'血量'+self.hp+'一碰就炸,攻击力'+self.lihai+',地雷数量'+self.shuliang
        return p
    def xiao(self):
        print('%s哈哈大笑一副大义凛然的样子'% self.name)
    def zha(self):
        print('僵尸来了，踩到我了，哈哈哈，轰的一声')
        print('僵尸的脚步被拖延了')
xiaolei=dilei('小地雷','黑','1','500','10')
print(xiaolei)
xiaolei.xiao()
xiaolei.zha()
class jiangshi:
    def __init__(self,name,yanse,hp,lihai,shuliang):
        self.name=name
        self.yanse=yanse
        self.hp=hp
        self.lihai=lihai
        self.shuliang=shuliang
    def __str__(self):
        j=self.name+'大boss出来了,'+self.yanse+'主角光环,'+'血量'+self.hp+',攻击力'+self.lihai+',数量'+self.shuliang
        return j
    def eat(self):
        print('僵尸们在%s的带领下,嗷嗷的向前冲..嗷嗷....' % self.name)
    def chong(self):
        print('僵尸们疯狂的撕咬着面前的一切植物')
        print('豌豆以沦陷，只剩下了小地雷')
    def tiao(self):
        print('%s欢快的一跳一跳的向着脑子跳去。。。'% self.name)
    def lunxian(self):
        print('啊.....好吃，沦陷了，朕的植物王国..')
shi1=jiangshi('大力僵尸','红色','500','1000','20')
print(shi1)
shi1.eat()
shi1.chong()
shi2=jiangshi('飞天蹦蹦僵尸','紫色','300','500','30')
print(shi2)
shi2.tiao()
shi2.lunxian()
