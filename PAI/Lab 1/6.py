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