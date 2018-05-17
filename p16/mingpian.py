ming_list = [] #f创建一个列表
def systemmenu():
    print("菜单展示")
    print("*"*32)

    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("4.编辑名片")
    print("5.退出系统")

    print("*"*32)
def xinjian():
    print("*"*45)
    print("请创建一个名片：")
    name=input("请输入您的名字：")
    age=input("请输入您的的年龄：")
    company=input("请输入您所在的公司：")
    title=input("请输入您的职位：")
    phone=input("请输入您的电话号码：")
    address=input("请输入您的地址：")
    dictionary={}
    dictionary['name']=name#插入数据到dictionary字典中
    dictionary['age']=age#同上
    dictionary['company']=company#同上
    dictionary['title']=title#同上
    dictionary['phone']=phone#同上
    dictionary['address']=address#同上
    ming_list.append(dictionary)#把dictionary字典追加到列表中
    print("创建成功请查看")
    print(" name: %s \n age: %s \n company: %s\n title: %s \n phone: %s \n address: %s \n" % (dictionary['name'], dictionary['age'], dictionary['company'] ,dictionary['title'] ,dictionary['phone'] ,dictionary['address']))
def xianshi():
    print(ming_list ,end="\n")
def chaxun():
    uu=input("请输入你要查询的姓名：")
    for zidian in ming_list:
        if uu == zidian["name"]:
            print("您的名字是：%s \n 您的年龄是：%s \n您所在的公司是：%s\n您的职位是：%s\n您的号码是：%s\n您的地址是：%s\n" % (zidian['name'],zidian['age'],zidian['company'],zidian['title'],zidian['phone'],zidian['address']))   
        while uu != zidian['name']:
            uu=print("用户不存在，请重新输入")
def bianji():
    qq=input("请输入您是要操作的对象：1（删除名片）2（编辑名片）")
    if qq == '1':
        for zidian in ming_list:
            rr=input("请输入你要删除的姓名：")
            if rr == zidian['name']:
                ming_list.remove(zidian)
                print("删除成功")
    elif qq == '2':
        for zidian in ming_list:
            aa=input("请输入您要修改的人的名字：")
            if aa == zidian['name']:
                ww=int(imput("请输入你要编辑的对象1（名字）2（年龄）3（公司）4（职位）5（号码）6（地址），请按序号输出："))
                if ww == '1':
                    zidian['name']=aa
                elif ww == '2':
                    zidian['age']=aa
                elif ww == '3':
                    zidian["company"]=aa
                elif ww == '3':
                    zidian["title"]=aa
                elif ww == '4':
                    zidian["phone"]=aa
                elif ww == '5':
                    zidian["address"]=aa
                while (ww != '1' and ww != '2') and (ww != '3' and ww != '4') and (ww != '5' and ww != '6'):
                    ww=(input("输入错误，请按照规格重新输入"))
        while aa != zidian['name']:
            aa=input("用户不存在请重新输入：")
    while qq != '1' and qq != '2':
        qq=input("输入出错，请按照格式重新输入：")

def tuichu():
    print("成功退出系统")
while True:
    systemmenu()
    user=int(input("请选择你要操作的对象"))
    if user == 1:
        xinjian()
    elif user== 2:
        xianshi()
    elif user == 3:
        chaxun()
    elif user == 4:
        bianji()
    else:
        tuichu()
        break 
