# Question 1


students = []

n = int(input("enter no students: "))
m = int(input("enter no subs: "))

for i in range(n):
    name = input("enter name: ")
    marks = []

    for j in range(m):
        marks.append(float(input("enter marks: ")))

    avg = sum(marks) / m
    students.append([name, avg])

highest = max(students, key=lambda x: x[1])

print("highest:", highest[0])
print("average:", highest[1])

threshold = float(input("enter threshold: "))

print("students abv threshold:")
for student in students:
    if student[1] > threshold:
        print(student[0])

# Question 2



products = {
    101: ["Laptop", "Electronics", 800, 10],
    102: ["Phone", "Electronics", 500, 0],
    103: ["Shoes", "Fashion", 80, 5]
}

print(products[101])

products[101][2] = 750
products[102][3] = 20

for id, p in products.items():
    if p[3] == 0:
        print("Out of stock:", p[0])

# Question 3
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

# Question 4
course_a = set(input("Enter Course A IDs: ").split())
course_b = set(input("Enter Course B IDs: ").split())

print("Both:", course_a & course_b)
print("Only A:", course_a - course_b)
print("Only B:", course_b - course_a)
print("All:", course_a | course_b)

# Question 5


emp = {}

n = int(input("Enter no employees: "))

for i in range(n):
    eid = input("enter employee ID: ")
    emp[eid] = {
        "name": input("enter name: "),
        "department": input("enter dept: "),
        "salary": float(input("enter salary: ")),
        "job_title": input("enter title: ")
    }

eid = input("enter ID for search: ")
print(emp.get(eid, "Not found"))

eid = input("Enter ID to update salary: ")
if eid in emp:
    emp[eid]["salary"] = float(input("enter new salary: "))

eid = input("enter ID to add: ")
emp[eid] = {
    "name": input("enter name: "),
    "department": input("enter department: "),
    "salary": float(input("enter salary: ")),
    "job_title": input("enter job title: ")
}

eid = input("Enter ID for remove: ")
emp.pop(eid, None)

# Question 6


logs = input("Enter logs: ").split()

count = {}

for log in logs:
    count[log] = count.get(log, 0) + 1

print("Count:", count)
print("Log types:", set(logs))

most = max(count, key=count.get)
print("Most frequent:", most)

# Question 7


cart = {}

def add_product(pid, price, qty):
    if pid in cart:
        cart[pid]["qty"] += qty
    else:
        cart[pid] = {"price": price, "qty": qty}

def remove_product(pid):
    cart.pop(pid, None)

def update_quantity(pid, qty):
    if pid in cart:
        cart[pid]["qty"] = qty

def total():
    return sum(item["price"] * item["qty"] for item in cart.values())

add_product("P1", 100, 2)
add_product("P2", 50, 3)

update_quantity("P1", 4)
remove_product("P2")

print("Total:", total())

# Question 8


emails = [
    "ali@gmail.com", "ali@yahoo.com", "ahmed@gmail.com",
    "taha@gmail.com", "ali@yahoo.com", "zayyan@hotmail.com"
]

unique = list(dict.fromkeys(emails))

print(unique)

# Question 9


config = (
    "App",
    "1.6",
    ("Windows", "Linux", "Mac"),
    ("localhost", 3306)
)

print(config)

try:
    config[0] = "NewApp"
except TypeError as e:
    print("cant modify:", e)


# Question 10


employees = [
    ("E101", "Ali", "IT", 85000),
    ("E102", "Sara", "HR", 75000),
    ("E103", "Ahmed", "IT", 95000),
    ("E104", "Zain", "Finance", 90000)
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
