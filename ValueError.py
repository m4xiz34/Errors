try:
    number = int(input("Enter your number here: "))
    print(number, "is valid.")
except ValueError as ex:
    print("Exception:", ex)
    
