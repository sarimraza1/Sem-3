listt = list(input("Enter numbers: ").split())

large = int(listt[0])

for n in listt:

    if int(n) > large:
        large = int(n)

print("largest no:", large)