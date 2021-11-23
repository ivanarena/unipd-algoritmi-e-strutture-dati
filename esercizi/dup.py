# Realizzare una funzione Dup(A, p, r) che verifica, in modo divide et impera, la presenza di duplicati nell'array A, restituendo un booleano.
# Estenderla ad una funzione DupCount(A,p,r) che conti il numero di duplicati, ovvero il numero di coppie { (i, j) ∣ i != j && A[i] = A[j] }.

numbers = [9, 4, 2, 6, 1, 3, 5, 3]


def merge(A, start, mid, end):
    left = A[start:mid+1]
    right = A[mid+1:end+1]

    check = False  # flag

    l = r = 0  # contatori di left e right
    k = start  # contatore dell'array originale

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            A[k] = left[l]
            l += 1
        elif left[l] > right[r]:
            A[k] = right[r]
            r += 1
        elif left[l] == right[r]:
            A[k] = left[l]
            l += 1
            check = True  # duplicato trovato
        k += 1

    while l < len(left):
        A[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        A[k] = right[r]
        r += 1
        k += 1

    return check


# Dup(A, p, r)
def dup(A, start, end):
    if end - start >= 1:
        mid = (start + end) // 2
        return dup(A, start, mid) or dup(A, mid + 1, end) or merge(A, start, mid, end)
    else:
        return False


print('numbers:', numbers)
print(dup(numbers, 0, len(numbers) - 1))
print('sorted:', numbers)
