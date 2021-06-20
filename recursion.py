def binary_search(start, end, list_item, item):
    if start > end:
        return -1
    mid = (int)((start + end) / 2)
    if list_item[mid] == item:
        return mid
    if item > list_item[mid]:
        return binary_search(mid + 1, end, list_item, item)
    else:
        return binary_search(start, mid - 1, list_item, item)


def bin_search(list_item, item):
    return binary_search(0, len(list_item) - 1, list_item, item)


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]
    print(bin_search(my_list, 9))
    print(bin_search(my_list, -1))
