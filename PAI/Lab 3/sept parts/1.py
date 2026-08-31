text = """
hello how what when why when what hello  yes no no no no low high                                                                   
"""

words = text.lower().split()
                         

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:", frequency)


most_frequent = max(frequency, key=frequency.get)
print("Most frequent word:", most_frequent)


unique_words = set(words)
print("Unique words:", unique_words)


print("Words appearing more than once:")

for word in frequency:
    if frequency[word] > 1:
        print(word)

