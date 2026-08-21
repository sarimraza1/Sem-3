listt = list(input("Enter numbers: ").split())

total = 0

for n in listt:
    total = total + int(n)

print("sum:", total)