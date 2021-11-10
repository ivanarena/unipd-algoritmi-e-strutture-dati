numbers = [9, 4, 5, 6, 1, 7, 2, 5]


def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1


print('numbers', numbers)
merge_sort(numbers)
print('sorted:', numbers)
