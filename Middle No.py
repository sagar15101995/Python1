a=int(input("Enter 1st Number"))
b=int(input("ENter 2nd number"))
c=int(input("Enter 3rd number"))
if (a>b) and (a<c) or (a<b) and (a>c):
    print("Middle Number",a)
elif (b>a) and (b<c) or (b<a) and (b>c):
    print("Middle No is",b)
else:
    print("Middle No is",c)
