#building a calcilator

a=int(input("Enter your number here " ))
operation = input("what operation do you want to perform ")
b=int(input("Enter your number here " ))
if operation=="add" or operation=="+":
    sum_ab = a + b
    print("the sum of the given number is", sum_ab)
elif operation=="sub" or operation=="-":
    sub_ab = a - b
    print("the difference of the given number is", sub_ab)
elif operation=="divide" or operation=="/":
    if b==0:
        print("number cant be divided by zero")

    else:
        div_ab = a / b
        print("the division of the given number is", div_ab)

elif operation=="multiply" or operation=="*":

    prod_ab = a * b
    print("the product of the given number is", prod_ab)