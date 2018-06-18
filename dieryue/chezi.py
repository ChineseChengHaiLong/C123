class House:
    def __init__(self,area,address):
        self.area=area
        self.address=address
        self.jiju=[]
        
    def set_A(self,jia):
        if int(self.area) > int(jia.area):
            self.area=self.area-jia.area
            self.jiju.append(jia.name)
        else:
            print('家具太大放不下')
    def __str__(self):
        name = ''
        for i in self.jiju:
            name = name + i +','
        name=name.strip(',')
        s =( '房子现在可使用大小是%d平方，房子的地址在%s,房子里的家具有%s' % (self.area,self.address,name))
        return s
class Bed:
    def __init__(self,area,name):
        self.area=area
        self.name=name
    def __str__(self):
        d= ('床的大小是%s平米，床的名字是%s' % (self.area,self.name)) 
        return d
bed_yi=int(input('请输入您购买房子的大小：'))
ad_re=input('请输入您房子的地址：')
bedone=int(input('请输入您要购买床的大小：'))
bedname=input('请输入您要购买床的名字:')
house1=House(bed_yi,ad_re)
print(house1)
bed1=Bed(bedone,bedname)
print(bed1)
house1.set_A(bed1)
print(house1)

