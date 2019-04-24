import cmath
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
d=(b**2)-(4*a*c)
r1=(-b-cmath.sqrt(d))/(2*a)
r2=(-b+cmath.sqrt(d))/(2*a)
print("The roots of the equation are {} and {}".format(r1,r2))
