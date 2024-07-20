def odd_index_sum(numbers):
    total = 0
    for i in range(1, len(numbers), 2):
        total += numbers[i]
    return total



sample_list = [1, 2, 3, 4, 5, 6]
result = odd_index_sum(sample_list)
print(result)

