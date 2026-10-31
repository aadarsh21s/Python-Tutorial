x=int(input("Enter the value of x:"))
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case 4:
        print("x is 4")
    case _ if x!=40:
        print(x, "is not equal to 40")
    case _ if x!=50:
        print(x, "is not equal to 50")
    case _:
        print(x)
        
