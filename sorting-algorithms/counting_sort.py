# NOTE: numbers as intented to be non-negative

numbers = [2, 3, 4, 1, 5, 2, 3, 2]


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


print("array:", numbers)
numbers = counting_sort(numbers)
print("sorted:", numbers)
