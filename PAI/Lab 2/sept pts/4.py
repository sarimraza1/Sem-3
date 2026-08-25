course_a = set(input("Enter Course A IDs: ").split())
course_b = set(input("Enter Course B IDs: ").split())

print("Both:", course_a & course_b)
print("Only A:", course_a - course_b)
print("Only B:", course_b - course_a)
print("All:", course_a | course_b)
