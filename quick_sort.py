def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        array_less = quick_sort(less)
        array_greater = quick_sort(greater)
        return array_less + [pivot] + array_greater


if __name__ == "__main__":
    print(quick_sort([10, 5, 2, 3, 11]))
