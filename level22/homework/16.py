def longest_string(strings):
    if not strings:
        return None
    longest = strings[0]
    for a in strings:
        if len(a) > len(longest):
            longest = a
    return longest


strings = ["apple", "banana", "orange", "kiwi"]
result = longest_string(strings)

print(result)  
