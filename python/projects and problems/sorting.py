def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls to sort the two halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add the remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result




print(merge_sort([1,5,1,5,1,9,7,5,6,8,4,3,1,3,5,6,8,3,1,19,345,234,12,35]))
print(bubble_sort([1,5,1,5,1,9,7,5,6,8,4,3,1,3,5,6,8,3,1,19,345,234,12,35]))