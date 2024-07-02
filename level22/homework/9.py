def min_difference(list1, list2):
    if not list1 or not list2:
        return ValueError("Both lists must have at least one number")
    
    min_diff = float

    for num1 in list1:
        for num2 in list2:
            min_diff = (num1 - num2)

    return min_diff


list1 = [1, 3, 15, 11, 2]
list2 = [23, 127, 235, 19, 8]
result = min_difference(list1, list2)

print(result)  
