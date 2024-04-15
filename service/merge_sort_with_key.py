from domain.entities import Book, Client
from domain.library import Inchiriere


def merge(arr1, arr2, key):
    result = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if key(arr1[i]) < key(arr2[j]):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result


def merge_sort_with_key(my_list, key=lambda x: x):
    list_length = len(my_list)

    if list_length <= 1:
        return my_list

    middle = list_length // 2

    left = my_list[:middle]
    right = my_list[middle:]

    sorted_left = merge_sort_with_key(left, key)
    sorted_right = merge_sort_with_key(right, key)

    return merge(sorted_left, sorted_right, key)
