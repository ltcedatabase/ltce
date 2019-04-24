print("Enter numerator and denominator")
a,b=map(int,input().split())
try:
   quotient=a/b
   print("quotient is:-",quotient)
except ZeroDivisionError:
   print("cant divide the number by zero")
