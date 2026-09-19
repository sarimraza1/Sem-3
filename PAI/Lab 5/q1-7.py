# Question 1

with open("experiments.txt", "w") as file:
    file.write("AI1,abby,set1,0.1,20\n")
    file.write("AI2,dabby,set2,0.2,30\n")

with open("experiments.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

id = input("enter id to search: ")
found = False

for line in lines:
    x = line.strip().split(",")
    if x[0] == id:
        print(line.strip())
        found = True

if not found:
    print("not found")

id = input("enter new id: ")
model = input("enter model: ")
dataset = input("enter dataset: ")
rate = input("enter rate: ")
epochs = input("enter epochs: ")

with open("experiments.txt", "a") as file:
    file.write(id + "," + model + "," + dataset + "," + rate + "," + epochs + "\n")

id = input("enter id to update: ")

with open("experiments.txt", "r") as file:
    lines = file.readlines()

found = False

for i in range(len(lines)):
    x = lines[i].strip().split(",")

    if x[0] == id:
        model = input("enter new model: ")
        dataset = input("enter new dataset: ")
        rate = input("enter new rate: ")
        epochs = input("enter new epochs: ")
        lines[i] = id + "," + model + "," + dataset + "," + rate + "," + epochs + "\n"
        found = True

if not found:
    print("not found")

with open("experiments.txt", "w") as file:
    file.writelines(lines)

id = input("enter id to remove: ")

with open("experiments.txt", "r") as file:
    lines = file.readlines()

new = []
found = False

for line in lines:
    x = line.strip().split(",")

    if x[0] == id:
        found = True
    else:
        new.append(line)

if not found:
    print("not found")

with open("experiments.txt", "w") as file:
    file.writelines(new)


# Question 2

import csv

with open("patients.csv", "w", newline="") as file:
    w = csv.writer(file)
    w.writerow(["id", "age", "bmi", "bp", "glucose", "label"])
    w.writerow(["P1", 20, 22, 110, 90, 0])
    w.writerow(["P2", 35, 28, 125, 140, 1])

with open("patients.csv", "r") as file:
    r = csv.DictReader(file)
    data = list(r)

for x in data:
    print(x)

pos = 0
neg = 0
bmi = 0
glucose = 0

for x in data:
    if x["label"] == "1":
        pos += 1
    else:
        neg += 1

    bmi += float(x["bmi"])
    glucose += float(x["glucose"])

print("positive:", pos)
print("negative:", neg)
print("average bmi:", bmi / len(data))
print("average glucose:", glucose / len(data))

limit = float(input("enter glucose limit: "))

for x in data:
    if float(x["glucose"]) > limit:
        print(x)

id = input("enter new id: ")
age = input("enter age: ")
bmi = input("enter bmi: ")
bp = input("enter bp: ")
glucose = input("enter glucose: ")
label = input("enter label: ")

with open("patients.csv", "a", newline="") as file:
    w = csv.writer(file)
    w.writerow([id, age, bmi, bp, glucose, label])

with open("patients.csv", "r") as file:
    r = csv.DictReader(file)
    data = list(r)

id = input("enter id to update: ")
found = False

for x in data:
    if x["id"] == id:
        x["age"] = input("enter new age: ")
        x["bmi"] = input("enter new bmi: ")
        x["bp"] = input("enter new bp: ")
        x["glucose"] = input("enter new glucose: ")
        x["label"] = input("enter new label: ")
        found = True

if not found:
    print("not found")

with open("patients.csv", "w", newline="") as file:
    w = csv.DictWriter(file, fieldnames=["id", "age", "bmi", "bp", "glucose", "label"])
    w.writeheader()
    w.writerows(data)


# Question 3

import json

data = [
    {"model": "abby", "accuracy": 0.8, "precision": 0.7, "recall": 0.8, "f1": 0.7},
    {"model": "dabby", "accuracy": 0.9, "precision": 0.8, "recall": 0.7, "f1": 0.8}
]

with open("model_results.json", "w") as file:
    json.dump(data, file)

with open("model_results.json", "r") as file:
    data = json.load(file)

bestA = data[0]
bestF = data[0]

for x in data:
    if x["accuracy"] > bestA["accuracy"]:
        bestA = x

    if x["f1"] > bestF["f1"]:
        bestF = x

print("highest accuracy:", bestA["model"])
print("highest f1:", bestF["model"])

model = input("enter new model: ")
acc = float(input("enter accuracy: "))
pre = float(input("enter precision: "))
rec = float(input("enter recall: "))
f1 = float(input("enter f1: "))

data.append({
    "model": model,
    "accuracy": acc,
    "precision": pre,
    "recall": rec,
    "f1": f1
})

name = input("enter model to update: ")
found = False

for x in data:
    if x["model"] == name:
        x["accuracy"] = float(input("enter new accuracy: "))
        x["precision"] = float(input("enter new precision: "))
        x["recall"] = float(input("enter new recall: "))
        x["f1"] = float(input("enter new f1: "))
        found = True

if not found:
    print("not found")

name = input("enter model to remove: ")
new = []
found = False

for x in data:
    if x["model"] == name:
        found = True
    else:
        new.append(x)

if not found:
    print("not found")

with open("model_results.json", "w") as file:
    json.dump(new, file)


# Question 4

import requests

try:
    r = requests.get(
        "https://moltstreet.com/api/v1/signals/actionable",
        params={"limit": 1},
        timeout=5
    )

    print("status:", r.status_code)
    r.raise_for_status()

    data = r.json()
    x = data["data"]["signals"][0]

    print("input:", x["ticker"])
    print("prediction:", x["direction"])
    print("confidence:", x["confidence"])

except requests.exceptions.Timeout:
    print("request timed out")

except requests.exceptions.ConnectionError:
    print("connection error")

except requests.exceptions.HTTPError:
    print("http error")

except (ValueError, KeyError, IndexError):
    print("invalid response")


# Question 5

try:
    id = input("enter post id: ")

    r = requests.get(
        "https://jsonplaceholder.typicode.com/comments",
        params={"postId": id},
        timeout=5
    )

    print("status:", r.status_code)
    r.raise_for_status()

    data = r.json()[:2]

    for x in data:
        print("text:", x["body"])
        print("source:", x["email"])
        print("name:", x["name"])

    with open("text.json", "w") as file:
        json.dump(data, file)

    with open("text.csv", "w", newline="") as file:
        w = csv.writer(file)
        w.writerow(["text", "source", "name"])

        for x in data:
            w.writerow([x["body"], x["email"], x["name"]])

except requests.exceptions.Timeout:
    print("request timed out")

except requests.exceptions.ConnectionError:
    print("connection error")

except requests.exceptions.HTTPError:
    print("http error")

except ValueError:
    print("invalid response")

except OSError:
    print("file error")


# Question 6

try:
    url = "https://jsonplaceholder.typicode.com/posts"

    r = requests.get(url + "/1", timeout=5)
    print("get:", r.status_code)
    print(r.json())

    data = {
        "image": "pic1.jpg",
        "prediction": "cat"
    }

    r = requests.post(url, json=data, timeout=5)
    print("post:", r.status_code)
    print(r.json())

    data = {
        "image": "pic1.jpg",
        "prediction": "dog"
    }

    r = requests.put(url + "/1", json=data, timeout=5)
    print("put:", r.status_code)
    print(r.json())

    r = requests.delete(url + "/1", timeout=5)
    print("delete:", r.status_code)

except requests.exceptions.Timeout:
    print("request timed out")

except requests.exceptions.ConnectionError:
    print("connection error")

except requests.exceptions.HTTPError:
    print("http error")

except requests.exceptions.RequestException:
    print("request failed")

except ValueError:
    print("invalid response")


# Question 7

try:
    topic = input("enter topic: ")

    r = requests.get(
        "https://api.openalex.org/works",
        params={"search": topic, "per-page": 2},
        timeout=5
    )

    print("status:", r.status_code)
    r.raise_for_status()

    data = r.json()["results"]
    save = []

    for x in data:
        save.append({
            "title": x["title"],
            "score": x["cited_by_count"]
        })

    highest = save[0]

    for x in save:
        if x["score"] > highest["score"]:
            highest = x

    print("highest:", highest)

    with open("ai_data.json", "w") as file:
        json.dump(save, file)

    with open("ai_data.csv", "w", newline="") as file:
        w = csv.writer(file)
        w.writerow(["title", "score"])

        for x in save:
            w.writerow([x["title"], x["score"]])

except requests.exceptions.Timeout:
    print("request timed out")

except requests.exceptions.ConnectionError:
    print("connection error")

except requests.exceptions.HTTPError:
    print("http error")

except ValueError:
    print("invalid response")

except OSError:
    print("file error")

else:
    try:
        with open("ai_data.json", "r") as file:
            a = json.load(file)

        with open("ai_data.csv", "r") as file:
            b = list(csv.reader(file))

        print(a)
        print(b)

    except FileNotFoundError:
        print("file not found")

    except json.JSONDecodeError:
        print("invalid json")

finally:
    print("done")