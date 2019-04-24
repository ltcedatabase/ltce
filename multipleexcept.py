try:
    number=int(input("Enter a number"))
    print("square of the number is:-",number**2)
    
except KeyboardInterrupt:
    print("You should have entered a number.....program Terminating..")
    
except ValueError:
    print("Err..numbers only")
    
    print("Bye")    
