# Realizzare una versione ricorsiva della funzione InsertionSort.

numbers = [9, 4, 5, 6, 1, 7, 2, 5]


def insert(items, key):
    if key > 0 and items[key - 1] > items[key]:
        items[key], items[key - 1] = items[key - 1], items[key]
        insert(items, key - 1)


def insertion_sort_ricorsivo(items, key):
    if key > 0:  # list unsorted
        insertion_sort_ricorsivo(items, key - 1)  # ordina items[0..key - 1]
        insert(items, key)  # inserisce key al posto giusto


print('numbers:', numbers)
insertion_sort_ricorsivo(numbers, len(numbers) - 1)
print('sorted:', numbers)

# DIMOSTRAZIONE DI CORRETTEZZA:

# insertion_sort_ricorsivo:
# (key = 0) L'array contiene un solo elemento ed è dunque ordinato;
# (key > 0) La chiamata ricorsiva ordina items[0..key - 1] e insert inserisce key al posto giusto
# quindi items ha un elemento in più ed è ancora ordinato (items[0..key] ordinato);

# insert:
# (key = 0) items[key] è l'elemento più piccolo ed è in items[0], quindi è ordinato;
# (key > 0) (1) items[key - 1] è minore di items[key], quindi items[key] è già al suo posto;
#           (2) items[key - 1] è maggiore di items[key], quindi avviene uno scambio che ordina
#               items[key - 1]; la successiva chiamata ricorsiva ordina anche items[key];
