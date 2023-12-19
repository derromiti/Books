# Problem: Sorting
# Input: A sequence of n keys a1,...,an.
# Output: The permutation (reordering) of the input sequence such that a' 1 ≤ a' 2 ≤···≤ a' r−1 ≤ a'n.


def insert_sort(items: list, n):
    for i in range(n):
        j = i
        while (j > 0) and (items[j] < items[j - 1]):
            # swap them
            a = items[j]
            b = items[j - 1]

            items[j] = b
            items[j - 1] = a

            j -= 1
    return items


if __name__ == "__main__":
    # Works for numbers
    items = [4, 2, 1, 5, 6, 6, 2, 3, 5, 2, 0, 182, 2, 52, 5]

    n = len(items)
    print(f"Start:  {items}")

    result = insert_sort(items, n)
    print(f"Result: {result}")

    # And for strings
    items = ["Mike", "Bob", "Sally", "Jill", "Jan"]

    n = len(items)
    print(f"Start:  {items}")

    result = insert_sort(items, n)
    print(f"Result: {result}")
