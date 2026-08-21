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