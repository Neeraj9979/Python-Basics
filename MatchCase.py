colour=input("Enter a Colour:")
match (colour):
    case "Red":
        print("Stop")
    case "Yellow":
        print("Look")
    case "Green":
        print("Go")
    case _:                   #Default
        print("Wrong Choice")