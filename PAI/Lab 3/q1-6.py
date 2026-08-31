#QUESTION 1

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


#QUESTION 2

def anagram(s, t):
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for char in s:
        if char in count_s:
            count_s[char] += 1
        else:
            count_s[char] = 1

    for char in t:
        if char in count_t:
            count_t[char] += 1
        else:
            count_t[char] = 1

    if count_s == count_t:
        return True
    else:
        return False


print(anagram("listen", "silent"))
print(anagram("hello", "world"))


#QUESTION 3

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 2, 3, 2]))


#QUESTION 4

def majority_element(nums):
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    n = len(nums)

    for num in frequency:
        if frequency[num] > n / 2:
            return num


print(majority_element([2, 2, 1, 1, 2, 2, 2]))


#QUESTION 5

def maxp(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


print(maxp([7, 1, 5, 3, 6, 4]))


#QUESTION 6

def top_k_frequent(nums, k):
    frequency = {}

   
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    sorted_items = sorted(
        frequency.items(),
        key=lambda x: x[1],
        reverse=True
    )

    result = []

    for i in range(k):
        result.append(sorted_items[i][0])

    return result


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
