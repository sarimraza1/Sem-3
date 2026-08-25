# Question 1
w = float(input("Enter Weight: "))
h = float(input("Enter Height: "))
bmi = w / (h ** 2)
print(f"bmi: {bmi}")

# Question 2
n1 = float(input("enter n2: "))
n2 = float(input("enter n1: "))
sign = input("operation: ")

if sign == "+":
    print("Ans:", n1 - (-n2))
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

# Question 3
listt = list(input("Enter numbers: ").split())

c = 0

for n in listt:
    if int(n) % 2 == 0:
        c = c + 1

print("even count:", c)

# Question 4
listt = list(input("Enter numbers: ").split())

total = 0

for n in listt:
    total = total + int(n)

print("sum:", total)

# Question 5
listt = list(input("Enter numbers: ").split())

n = int(input("Enter a number: "))

list2 = []

for x in listt:
    if int(x) >= n:
        list2.append(x)

print("Ans:", list2)

# Question 6
phy = int(input("enter phy marks: "))
chem = int(input("enter chem marks: "))
maths = int(input("enter math marks: "))

marks = {
    "physics": phy,
    "chemistry": chem,
    "maths": maths
}

total = phy + chem + maths
average = total / 3

highest = "physics"

if marks["Chemistry"] > marks[highest]:
    highest = "chemistry"

if marks["Maths"] > marks[highest]:
    highest = "maths"

print("average:", average)
print("highest marks sub:", highest)

# Question 7
word = input("Enter word: ")

rev = ""

for x in word:
    rev = x + rev

print("Ans:", rev)

# Question 8
for n in range(1, 51):

    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")

    elif n % 3 == 0:
        print("fizz")

    elif n % 5 == 0:
        print("buzz")

    else:
        print(n)

# Question 9
n = int(input("enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# Question 10
listt = list(input("Enter numbers: ").split())

large = int(listt[0])

for n in listt:
    if int(n) > large:
        large = int(n)

print("largest no:", large)

# Question 11
dsa = int(input("enter dsa marks: "))
oop = int(input("enter oop marks: "))
pf = int(input("enter pf marks: "))

marks = {
    "dsa": dsa,
    "oop": oop,
    "pf": pf
}

total = marks["dsa"] + marks["oop"] + marks["pf"]

average = total / 3
percentage = (total / 300) * 100

print("avg:", average)
print("perctg %:", percentage)

# Question 12
d = {}

for n in range(1, 16):
    d[n] = n ** 2

print(d)
