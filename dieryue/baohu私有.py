class Mai:
    def __init__(self,name,jiaqian):
        self.name=name
        self.jiaqian=jiaqian
    def mai_ren(self,ren):
        if ren == '客人':
            return 200
        elif ren == '自家人':
            return 10
        else:
            return self.jiaqian
people=Mai('辣条','50')
s=people.mai_ren('自家人')
print(s)
s=people.mai_ren('客人')
print(s)
s=people.mai_ren('其他人')
print(s)
