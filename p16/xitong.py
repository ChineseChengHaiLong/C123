list_1=[]
list_2=[]
import random
def feilei():
    er=input("请问您有会员卡吗：1（有）2（没有）")
    ll = 0
    while  ll < 3:
        if er != '1' and er != '2':
            er=input('报错，请按照序号输入：')
            ll=ll+1    
    if er == '1':
        ad=input('请输入您的姓名:')
        for i in list_1:
            if ad == i['姓名']:
                print('尊敬的会员卡用户您将享受9.5折的购物优惠')
                aa=input('您要进入商品分区：请选择1（玩具）2（瓜果蔬菜）3（生活用品）编号输入：')
                if aa == '1':
                    oo=input("请输入您要购买的玩具：飞机  坦克  火炮")
                    if oo == '飞机':
                        pp=int(input('飞机玩具一个20块,请输入要买的个数：'))
                        bb = 20#飞机玩具一个20块
                        money = bb*pp*0.95
                        i['余额']=float(i['余额'])-money
                        print(money)
                    elif oo == '坦克':
                        bb = 25#坦克玩具一个25块
                        pp=int(input('坦克玩具一个25块,请输入要买的个数：'))
                        money = bb*pp*0.95
                        i['余额']=float(i['余额'])-money
                        print(money)
                    elif oo == '火炮':
                        bb = 30#火炮的单价是30块
                        pp=int(input('火炮玩具一个30块,请输入要买的个数：'))
                        money = bb*pp*0.95
                        i['余额']=float(i['余额'])-money
                        print(money)
                    dic2={}
                    dic2['种类']=oo
                    dic2['数量']=pp
                    dic2['价格']=bb
                    dic2['花费']=money
                    list_2.append(dic2)
                if aa == '2':
                    oo=input("请输入您要购买的瓜果蔬菜：大西瓜  菠萝  香蕉")
                    if oo == '大西瓜':
                        pp=int(input('大西瓜一个2块,请输入要买的个数：'))
                        bb = 2#大西一个2块
                        money = bb*pp*0.95
                        i['余额']=float(i['余额'])-money
                        a=a+money
                        print(money)
                    elif oo == '菠萝':
                        bb = 5#坦克玩具一个25块
                        pp=int(input('菠萝一个5块,请输入要买的个数：'))
                        money = bb*pp*0.95
                        i['余额']=float(i['余额'])-money
                        a=a+money
                        print(money)
                    elif oo == '香蕉':
                        bb = 3#火炮的单价是30块
                        pp=int(input('香蕉一个3块,请输入要买的个数：'))
                        money = bb*pp*0.95
                        i['余额']=float(i['余额'])-money
                        a=a+money
                        print(money)
                    dic3={}
                    dic3['种类']=oo
                    dic3['数量']=pp
                    dic3['价格']=bb
                    dic3['花费']=money
                    list_2.append(dic3)
         
                if aa == '3':
                    oo=input("请输入您要购买的生活用品：床  浴缸  床单")
                    if oo == '床':
                        pp=int(input('床的单价是5000,请输入要买的个数：'))
                        bb = 5000
                        money = bb*pp*0.95
                        i['余额']=float(i['余额'])-money
                        a=a+money
                        print(money)
                    elif oo == '浴缸':
                        bb = 3000
                        pp=int(input('浴缸3000一个，请输入要买的个数：'))
                        money = bb*pp*0.95
                        i['余额']=float(i['余额'])-money
                        a=a+money
                        print(money)
                    elif oo == '床单':
                        bb = 1000
                        pp=int(input('床单3000,请输入要买的个数：'))
                        money = bb*pp*0.95
                        i['余额']=float(i['余额'])-money
                        a=a+money
                        print(money)
                    dic4={}
                    dic4['种类']=oo
                    dic4['数量']=pp
                    dic4['价格']=bb
                    dic4['花费']=money
                    list_2.append(dic4)
    elif er == '2':
        aa=input('您要进入商品分区：请选择1（玩具）2（瓜果蔬菜）3（生活用品）编号输入：')
        if aa == '1':
            oo=input("请输入您要购买的玩具：飞机  坦克  火炮")
            if oo == '飞机':
                pp=int(input('飞机玩具一个20块,请输入要买的个数：'))
                bb = 20#飞机玩具一个20块
                money = bb*pp
                print(money)
            elif oo == '坦克':
                bb = 25#坦克玩具一个25块
                pp=int(input('坦克玩具一个25块,请输入要买的个数：'))
                money = bb*pp
                print(money)
            elif oo == '火炮':
                bb = 30#火炮的单价是30块
                pp=int(input('火炮玩具一个30块,请输入要买的个数：'))
                money = bb*pp
                print(money)
            dic2={}
            dic2['种类']=oo
            dic2['数量']=pp
            dic2['价格']=bb
            dic2['花费']=money
            list_2.append(dic2)
        if aa == '2':
            oo=input("请输入您要购买的瓜果蔬菜：大西瓜  菠萝  香蕉")
            if oo == '大西瓜':
                pp=int(input('大西瓜一个2块,请输入要买的个数：'))
                bb = 2#大西一个2块
                print(money)
            elif oo == '菠萝':
                bb = 5#坦克玩具一个25块
                pp=int(input('菠萝一个5块,请输入要买的个数：'))
                money = bb*pp
                print(money)
            elif oo == '香蕉':
                bb = 3#火炮的单价是30块
                pp=int(input('香蕉一个3块,请输入要买的个数：'))
                money = bb*pp
                print(money)
            dic3={}
            dic3['种类']=oo
            dic3['数量']=pp
            dic3['价格']=bb
            dic3['花费']=money
            list_2.append(dic3)
        if aa == '3':
            oo=input("请输入您要购买的生活用品：床  浴缸  床单")
            if oo == '床':
                pp=int(input('床的单价是5000,请输入要买的个数：'))
                bb = 5000
                money = bb*pp
                print(money)
            elif oo == '浴缸':
                bb = 3000
                pp=int(input('浴缸3000一个，请输入要买的个数：'))
                money = bb*pp
                print(money)
            elif oo == '床单':
                bb = 1000
                pp=int(input('床单3000,请输入要买的个数：'))
                money = bb*pp
                print(money)
            dic4={}
            dic4['种类']=oo
            dic4['数量']=pp
            dic4['价格']=bb
            dic4['花费']=money
            list_2.append(dic4)
def systemmnue():
    print('*'*40)
    print('欢迎使用超市购物系统')
    print('1.办理会员卡（享受购物9.5折优惠）')
    print('2.显示办卡人信息')
    print('3.购物')
    print("4.查看历史购物信息")
    print("5.修改办卡信息")
    print('6.退出')
    print('*'*40)
mmm=1
def banka():
    global mmm
    print('*************此卡是第%d张卡:' % mmm)
    mmm=mmm+1
    name=input('请输入您的姓名：')
    age=input('请输入您的年龄：')
    sex=input('请输入您的性别：')
    com=input('请输入您的公司：')
    title=input('请输入您的职位：')
    phone=input('请输入您的号码：')
    address=input("请输入您的地址：")
    password=input('请输入您的密码：')
    qian=int(input('请输入您会员卡充值的钱数：'))
    acount=random.randint(12345678,99999999)
    dic1={}
    dic1['姓名']=name
    dic1['年龄']=age
    dic1['性别']=sex
    dic1['公司']=com
    dic1['职位']=title
    dic1['联系号码']=phone
    dic1['地址']=address
    dic1['帐号']=acount
    dic1['密码']=password
    dic1['余额']=qian
    list_1.append(dic1)
    print('办理会员卡成功购物将享受9.5折优惠，请查看,请保存好您的帐号，您的帐号是：',acount)
    print('姓名：%s \n年龄: %s\n性别: %s\n公司: %s\n职位: %s\n地址: %s\n密码: %s\n联系号码: %s\n会员卡余额: %s\n会员卡帐号: %s' % (name,age,sex,com,title,address,password,phone,qian,acount)) 
       
    
    
def xianshi():
    for zidian in list_1:
        print('姓名：%s \n年龄: %s\n性别: %s\n公司: %s\n职位: %s\n地址: %s\n密码: %s\n联系号码: %s\n会员卡余额: %s\n会员卡帐号: %s' % (zidian['姓名'],zidian['年龄'],zidian['性别'],zidian['公司'],zidian['职位'],zidian['地址'],zidian['密码'],zidian['联系号码'],zidian['余额'],zidian['帐号'])) 

def gouwu():
    feilei()
def chakan():
    if len(list_2) > 0:
        for i in list_2:
            print('分类: %s' % i['种类'])
            print('数量: %s' % i['数量'])
            print('价格: %s' % i['价格'])
            print('花费: %s' % i['花费'])
def xiugai():
    qw=input("请输入编辑操作序号1（删除会员卡）2（修改会员卡）")
    if qw == '1':
        ppt=input('请输入您要修改的名字：')
        if len(list_1) > 0:
            for i in list_1:
                if ppt == i['姓名']:
                    list_1.remove(i)
    if qw == '2':
        if len(list_1) > 0:
            for i in list_1:
                 ss=input('请输入您要修改的名字：')
                 if ss == i['姓名']:
                     dd=input('请您选择您要修改的序号：1（姓名）2（年龄）3（性别）4（公司）5（职位）6（联系号码）7（地址）8（密码）  退出按‘q’键，谢谢： ') 
                     if dd == '1':
                         ff=input("请输入您修改后的名字：")
                         i['姓名']=ff
                     elif dd == '2':
                         gg=input('请输入您修改后的年龄：')
                         i['年龄']=gg
                     elif dd == '3':
                         hh=input('请输入您修改后的性别：')
                         i['性别']=hh
                     elif dd == '4':
                         jj=input('请输入您要修改后的公司')
                         i['公司']=jj
                     elif dd == '5':
                         po=input('请输入您修改后的职位：')
                         i['职位'] == po
                     elif dd == '6':
                         oi=input('请输入您要修改后的联系方式:')
                         i['联系方式']= oi
                     elif dd == '7':
                         iu=input('请输入您要修改的地址：')
                         i['地址']=iu
                     elif dd == '8':
                         uy=input('请输入您要修改的密码：')
                         i['密码']=uy
def tuichu():
    print('成功退出系统')

while True:
    systemmnue()
    qq=input('请选择您要操作的序号：')
    if qq == '1':
        banka()
    elif qq == '2':
        xianshi()
    elif qq == '3':
        feilei()
    elif qq == '4':
        chakan()
    elif qq == '5':
        xiugai()
    else:
        tuichu()
        break
