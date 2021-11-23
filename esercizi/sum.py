# Realizzare una funzione Sum(A, key) che dato un array A e un intero key verifica se questo è esprimibile
# come la somma di due elementi di A ovvero se vi sono indici i e j tali che key = A[i] + A[j].


numbers = [7, 1, 8, 5]
key = 11


def counting_sort(numbers):
    sorted_numbers = [0] * len(numbers)
    occurrences = [0] * (max(numbers) + 1)  # initialize occurences

    for num in numbers:  # count occurrences
        occurrences[num] = occurrences[num] + 1

    for j in range(1, len(occurrences)):  # sum every element with the previous
        occurrences[j] = occurrences[j] + occurrences[j-1]

    occurrences.insert(0, 0)  # shift occurrences by one
    occurrences.pop()  # shift occurrences by one

    for num in numbers:  # fill returned array
        sorted_numbers[occurrences[num]] = num
        occurrences[num] = occurrences[num] + 1

    return sorted_numbers


def sum(A, key):
    A = counting_sort(A)  # ordinamento in loco
    print('sorted:', A)
    i = 0
    j = len(A) - 1
    while j >= 0 and i <= j:
        if A[i] + A[j] == key:
            return [i, j]
        if A[i] + A[j] > key:
            i = 0
            j -= 1
        else:  # A[i] + A[j] < key
            i += 1
    return False


print('numbers:', numbers)
indexes = sum(numbers, key)
print('indici non trovati.') if indexes == False else print(
    f'indici: ({indexes[0]}, {indexes[1]})')
