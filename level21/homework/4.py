def merge_sorted_lists(list1, list2):
    combined_list = []
    a, b = 0, 0

    while a < len(list1) and b < len(list2):
        if list1[a] < list2[b]:
            combined_list.append(list1[a])
            a += 1
        else:
            combined_list.append(list2[b])
            b += 1

    while a < len(list1):
        combined_list.append(list1[a])
        a += 1

    while b < len(list2):
        combined_list.append(list2[b])
        b += 1

        return combined_list
    
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_sorted_lists(list1, list2)
print(result) 

        
    