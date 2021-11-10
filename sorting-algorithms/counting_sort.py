numbers = [2, 3, 1, 1, 1, 2, 6, 2]
sorted_numbers = [0, 0, 0, 0, 0, 0, 0, 0]


def counting_sort(list, sorted_numbers, max):
    occurrences = []
    for i in range(max + 1):  # initialize occurrences
        occurrences.append(0)

    for num in numbers:  # count occurrences
        occurrences[num] = occurrences[num] + 1

    for j in range(1, len(occurrences)):  # sum every element with the previous
        occurrences[j] = occurrences[j] + occurrences[j-1]

    occurrences.insert(0, 0)  # shift occurrences by one
    occurrences.pop()  # shift occurrences by one

    for num in numbers:  # fill returned array
        sorted_numbers[occurrences[num]] = num
        occurrences[num] = occurrences[num] + 1


print("array:", numbers)
counting_sort(numbers, sorted_numbers, max(numbers))
print("sorted:", sorted_numbers)
