try:
 print("division")
 try:
  quotient="abc"/"pqr"
 finally:
  print("in finally block, it is always executed")
except TypeError:
 print("TypeError:-Dividing Strings")
