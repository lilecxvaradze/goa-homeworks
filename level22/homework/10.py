def difference_max_min(numbers):
    if not numbers:
        return ("List must have at least one number")
    
    max_num = max(numbers)
    min_num = min(numbers)
    
    return max_num - min_num

numbers = [10, 3, 15, 7, 22]
result = difference_max_min(numbers)

print(result)  
