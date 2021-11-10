numbers = [9, 4, 5, 6, 1, 7, 2, 5]


def insertion_sort(numbers):
    for j in range(1, len(numbers)):
        key = numbers[j]
        prev = j - 1
        while (prev >= 0 and numbers[prev] > key):
            numbers[prev + 1] = numbers[prev]
            prev = prev - 1
        numbers[prev + 1] = key


print('numbers:', numbers)
insertion_sort(numbers)
print('sorted:', numbers)
