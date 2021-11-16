numbers = [9, 4, 5, 6, 1, 7, 2, 5]


def merge(items, left, right):
    l = r = 0
    k = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            items[k] = left[l]
            l += 1
        else:
            items[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        items[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        items[k] = right[r]
        r += 1
        k += 1


def merge_sort(items):
    if len(items) > 1:
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(items, left, right)


print('numbers:', numbers)
merge_sort(numbers)
print('sorted:', numbers)
