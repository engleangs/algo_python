def build_sequence(array, sequences, maxLengthIndex):
    result = []
    while maxLengthIndex is not None:
        result.insert(0,array[maxLengthIndex])
        maxLengthIndex = sequences[maxLengthIndex]

    return result


def binary_search(startIdx, endIdx, indices, array, num):
    if startIdx > endIdx:
        return startIdx
    middleIdx = (startIdx + endIdx) // 2
    if array[indices[middleIdx]] < num:
        startIdx = middleIdx + 1
    else:
        endIdx = middleIdx - 1
    return binary_search(startIdx, endIdx, indices, array, num)


def longest_increasing_subsequence(array):
    sequnces = [None for _ in array]
    indices = [None for _ in array]
    length = 0
    for i, num in enumerate(array):
        newLength = binary_search(1, length, indices, array, num)
        sequnces[i] = indices[newLength - 1]
        indices[newLength] = i
        length = max(length, newLength)
    return build_sequence(array, sequnces, indices[length])


if __name__ == "__main__":
    items = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
    ls = longest_increasing_subsequence(items)
    print("longest subsequences", ls)
