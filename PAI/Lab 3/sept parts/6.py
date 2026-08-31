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
