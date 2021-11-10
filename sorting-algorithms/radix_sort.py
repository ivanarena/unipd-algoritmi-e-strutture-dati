numbers = [329, 457, 657, 839, 439, 720, 355]
index = len(str(max(numbers))) - 1  # highest number of digits as index


def key_func(num):
    global index
    return int(str(num)[index])


def radix_sort(numbers):
    global index
    for i in range(index + 1):
        # sorts by digit index
        numbers.sort(key=key_func)
        print(numbers)
        index = index - 1


radix_sort(numbers)
