valid = False

while not valid:
    try:
        n = int(input("Enter number here: "))
        while n%2 == 0:
            print("BYE.")
    except ValueError:
        print("Invalid value.")
