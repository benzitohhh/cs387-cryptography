def convert_to_bits(n, pad):
    result = []
    while n > 0:
        if n % 2 == 0:               # reveals rightmost bit
            result = [0] + result
        else:
            result = [1] + result
        n = n / 2                   # shift right
        
    # ok now we have our binary chars
    # let's pad it with leading 0s
    while len(result) < pad:
        result = [0] + result
    return result

print convert_to_bits(16384, 16)


