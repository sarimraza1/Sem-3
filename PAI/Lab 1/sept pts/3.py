listt = list(input("Enter numbers: ").split())

c = 0

for n in listt:
    if int(n) % 2 == 0:
        c = c + 1

print("even count:", c)