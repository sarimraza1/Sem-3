n1 = float(input("enter n2: "))
n2 = float(input("enter n1: "))
sign = input("operation: ")

if sign == "+":
    print("Ans:", n1-(-n2))
elif sign == "-":
    print("Ans:", n1 - n2)
elif sign == "*":
    print("Ans:", n1 * n2)
elif sign == "/":
    if n2 != 0:
        print("Ans:", n1 / n2)
    else:
        print("not possible")
else:
    print("incorrect sign")