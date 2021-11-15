numbers = [9, 4, 5, 6, 1, 7, 2, 5]


def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]
        merge_sort(left)
        merge_sort(right)

        l = r = 0
        k = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                numbers[k] = left[l]
                l += 1
            else:
                numbers[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            numbers[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            numbers[k] = right[r]
            r += 1
            k += 1


print('numbers', numbers)
merge_sort(numbers)
print('sorted:', numbers)
