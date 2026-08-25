employees = [
    ("11", "Ali", "EE", 85000),
    ("12", "Rao", "CE", 75000),
    ("13", "Ayan", "FT", 95000),
    ("14", "Zayyan", "AI", 90000)
]

emp_dict = {e[0]: e for e in employees}

print("IT:", [e for e in employees if e[2] == "IT"])

avg = sum(e[3] for e in employees) / len(employees)
print("Avg salary:", avg)

print("Highest:", max(employees, key=lambda e: e[3]))

departments = {e[2] for e in employees}
print("Departments:", departments)

count = {}
for e in employees:
    count[e[2]] = count.get(e[2], 0) + 1
print("Dept count:", count)

eid = input("enter ID: ")
print(emp_dict.get(eid, "Not found"))
