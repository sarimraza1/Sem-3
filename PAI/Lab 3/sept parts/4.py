def majority_element(nums):
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    n = len(nums)

    for num in frequency:
        if frequency[num] > n / 2:
            return num


print(majority_element([2, 2, 1, 1, 2, 2, 2]))
