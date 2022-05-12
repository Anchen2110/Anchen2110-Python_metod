v=int(input("v=?"))
N=int(input("N=?"))

if v<50:
    x=5
elif v<100:
    x=15
elif v<150:
    x=25
else:
    x=35
c=x*N
print("c=",c)