import math

a=int(input("ingrese termino a:"))
b=int(input("ingrese termino b:"))
c=int(input("ingrese termnio c:"))

d=(b*b-4*a*c)

if a!=0:
    if d<0:
        print("las raices son imaginarias...")
    else:
        x1=(-b+(math.sqrt(d)))/(2*a)
        x2=(-b-(math.sqrt(d)))/(2*a)
        print("X1 = "+str(x1)+" X2 = "+str(x2))
else:
    print("coefiente a debe ser diferente de cero")
