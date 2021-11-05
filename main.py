def name(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
num1 = int(input("pls enter number 1\n"))
num2 = int(input("pls enter number 2\n"))
num3 = int(input("pls enter number 3\n"))
print(name(num1,num2,num3))
print("The greatest number is " + str(name(num1,num2,num3)))