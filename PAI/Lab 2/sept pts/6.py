logs = input("Enter logs: ").split()

count = {}

for log in logs:
    count[log] = count.get(log, 0) + 1

print("Count:", count)
print("Log types:", set(logs))

most = max(count, key=count.get)
print("Most frequent:", most)
