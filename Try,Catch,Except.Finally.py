try:
    x=int(input("Enter a number:"))
    ans = 10 / x
    
except ZeroDivisionError:
    print("You cannot divide by zero")

except ValueError:
    print("You cannot divide by string")

else:
    print(f"ans = {ans}")


finally:
    print("The program is completed!!!!")

