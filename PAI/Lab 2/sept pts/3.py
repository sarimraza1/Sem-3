trans = input("enter id: ").split()

unique = set()
duplicates = set()

for tid in trans:
    if tid in unique:
        duplicates.add(tid)
    else:
        unique.add(tid)

print("duplicates:", duplicates)
print("unique trans:", unique)
