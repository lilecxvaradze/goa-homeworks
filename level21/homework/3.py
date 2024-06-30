def count_symbols(line):
    symbol_count = {}
    for symbol in line:
        if symbol in symbol_count:
            symbol_count[symbol] += 1
        else:
            symbol_count[symbol] = 1
    return symbol_count

line = "3 + 5 * (2 - 8)"
result = count_symbols(line)
print(result)