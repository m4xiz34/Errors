try:
    number1=int(input("Enter your first number here: "))
    number2=int(input("Enter your second number here: "))
    x = number1/number2
    
    print(x)
    
except ZeroDivisionError:
    print("Don't divide with zeros.")

except ValueError:
    print("Enter a numerical value.")
    
except NameError as y:
    print("The Exception Error is,", y)
    
except:
    print("Some errors occured...")
    
finally:
    print("I will print no matter what. You can't ge rid of me.")
