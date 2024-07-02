def find_longest_string(strings):
    if not strings:
        return None
    longest_string = strings[0]
    for s in strings:
        if len(s) > len(longest_string):
            longest_string = s
    return longest_string


strings = ["Hello", "lile", "tskhvaradze", "gun", "goo"]
longest = find_longest_string(strings)

print(longest)  
