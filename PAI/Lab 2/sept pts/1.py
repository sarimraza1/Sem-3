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
