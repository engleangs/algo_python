def longest_common_substring(str1, str2):
    cell = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
    max_value = 0
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if (str1[i - 1] == str2[j - 1]):
                cell[i][j] = cell[i - 1][j - 1] + 1
            max_value = max(cell[i][j], max_value)
    return max_value


if __name__ == "__main__":
    print(longest_common_substring("fish", "hish"))
