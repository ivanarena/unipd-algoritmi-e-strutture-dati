numbers = [9, 4, 5, 6, 1, 7, 2, 5]


def merge(items, start, mid, end):
    left = items[start:mid+1]
    right = items[mid+1:end+1]

    l = r = 0  # left and right iterators
    k = start  # main list iterator

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            items[k] = left[l]
            l += 1
        else:
            items[k] = right[r]
            r += 1
        k += 1

    while l < len(left):  # add remaining items
        items[k] = left[l]
        l += 1
        k += 1

    while r < len(right):  # add remaining items
        items[k] = right[r]
        r += 1
        k += 1


def merge_sort(items, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(items, start, mid)
        merge_sort(items, mid + 1, end)
        merge(items, start, mid, end)


print('numbers:', numbers)
merge_sort(numbers, 0, len(numbers) - 1)
print('sorted:', numbers)
