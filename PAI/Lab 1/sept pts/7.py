word = input("Enter word: ")

rev = ""

for x in word:
    rev = x + rev

print("Ans:", rev)