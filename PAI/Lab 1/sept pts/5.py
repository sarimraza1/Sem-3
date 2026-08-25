listt = list(input("Enter numbers: ").split())

n = int(input("Enter a number: "))

list2 = []

for x in listt:
    if int(x) >= n:
        list2.append(x)

print("Ans:", list2)