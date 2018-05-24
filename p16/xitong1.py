import project1
while True:
    project1.systemmnue()
    qq=input('请选择您要操作的序号：')
    if qq == '1':
        project1.banka()
    elif qq == '2':
       project1.xianshi()
    elif qq == '3':
        project1.feilei()
    elif qq == '4':
        project1.chakan()
    elif qq == '5':
        project1.xiugai()
    else:
        project1.tuichu()
        break
