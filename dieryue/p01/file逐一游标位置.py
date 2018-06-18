f=open('shi.txt','w')
f.write('举杯邀明月\n把酒问青天\n不知天上宫阙\n今昔是何年\n')
f.close()
f=open('shi.txt','r')
a=f.readline()
b=f.tell()
print('第一行的是: %s' % a)
print('第一行的位置是: %d' % b)

