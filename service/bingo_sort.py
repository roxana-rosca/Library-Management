from domain.entities import Book, Client
from domain.library import Inchiriere


def bingo_sort(arr, key=lambda x: x):
    size = len(arr)
    # finding the smallest element from the array
    bingo = min(arr, key=key)

    # finding the largest element from the array
    largest = max(arr, key=key)
    next_bingo = largest
    next_pos = 0
    while key(bingo) < key(next_bingo):
        # will keep the track of the element position to shift to the correct position
        start_pos = next_pos
        for i in range(start_pos, size):
            if key(arr[i]) == key(bingo):
                arr[i], arr[next_pos] = arr[next_pos], arr[i]
                next_pos += 1
            elif key(arr[i]) < key(next_bingo):
                # here we are finding the next bingo element for the next pass
                next_bingo = key(arr[i])
        bingo = next_bingo
        next_bingo = largest
    return arr
