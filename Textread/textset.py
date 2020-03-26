setno = 4

f=open("picamerOption.txt", 'w')
if setno == 0:
    data="lowest"
elif setno == 1:
    data="ower"
elif setno == 2:
    data= "low"
elif setno == 3:
    data="middle"
elif setno == 4:
    data="high"
elif setno == 5:
    data="higher"
elif setno == 6:
    data="highest"
f.write(data)
f.close()