def find_smallest_number(numbers):
    if not numbers:
        return ("List must have at least one number")
    
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    
    return smallest


numbers = [10, 3, 15, 7, 22]
result = find_smallest_number(numbers)

print(result)  
