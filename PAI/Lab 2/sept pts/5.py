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
