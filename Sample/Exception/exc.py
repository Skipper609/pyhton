try:
    num1 = int(input("Enter num1 :"))
    num2 = int(input("Enter num2 :"))
    print(num1/num2)
    print("num1 "+num2)
except ValueError:
    print("Enter only numbers not charecters")
except ZeroDivisionError:
    print("Dont divide by zero")
except Exception as e:
    print(f"Ooops !!! went down !!!\n{e}")