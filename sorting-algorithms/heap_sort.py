numbers = [9, 4, 5, 6, 1, 7, 2, 5]

# NOTE -- HEAP:
# heap[1] = root
# heap[i] = node
# heap[2i] = i's left son
# heap[2i+1] = i's right son


def max_heapify(heap, parent, end):
    l = parent * 2
    r = parent * 2 + 1
    if end >= l and heap[l] > heap[parent]:
        max = l
    else:
        max = parent

    if end >= r and heap[r] > heap[max]:
        max = r

    if max != parent:
        heap[parent], heap[max] = heap[max], heap[parent]
        max_heapify(heap, max, end)


def build_max_heap(heap):
    # add temporary node to shift the heap so that it becomes heap[1..n] (n is at index = len(heap) - 1)
    heap.insert(0, -1)
    for i in range(len(heap) // 2, 0, -1):
        # NOTE "len(heap) - 1" because the temporary node adds one index
        max_heapify(heap, i, len(heap) - 1)


def heap_sort(numbers, start, end):
    build_max_heap(numbers)
    for i in range(end, 1, -1):
        numbers[1], numbers[i] = numbers[i], numbers[1]
        end = end - 1
        max_heapify(numbers, 1, end)
    numbers.pop(0)  # remove temporary node


print('numbers:', numbers)
heap_sort(numbers, 0, len(numbers))
print('sorted:', numbers)
