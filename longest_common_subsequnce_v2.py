def lc_subsequence(st1, st2):
    cell = [[1 for _ in range(0, len(st1))] for _ in range(0, len(st2))]
    for i in range(1, len(st1)):
        for j in range(1, len(st2)):
            ch1 = st1[i]
            ch2 = st2[j]
            if ch1 == ch2:
                cell[i][j] = cell[i - 1][j - 1] + 1
            else:
                cell[i][j] = max(cell[i - 1][j], cell[i][j - 1])
    return cell[len(st1) - 1][len(st2) - 1]


if __name__ == "__main__":
    print(lc_subsequence("FOSH", "FISH"))
