numbers = [9, 4, 5, 6, 1, 7, 2, 5]


def partition(numbers, start, end):
    pivot = numbers[end]
    i = start - 1
    for j in range(start, end):
        if numbers[j] <= pivot:
            i = i + 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[end] = numbers[end], numbers[i+1]  # swap with pivot
    return i+1


def quick_sort(numbers, start, end):
    if start < end:
        part = partition(numbers, start, end)
        quick_sort(numbers, start, part - 1)
        quick_sort(numbers, part + 1, end)


print('numbers', numbers)
quick_sort(numbers, 0, len(numbers) - 1)
print('sorted:', numbers)
