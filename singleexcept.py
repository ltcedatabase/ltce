try:
 print("Enter a number")
 num=int(input())
 square=num*num
 print("Square:- ",square)
 
except(KeyboardInterrupt, ValueError,TypeError):
  print("Plaese check the number before you enter")
print("Bye")