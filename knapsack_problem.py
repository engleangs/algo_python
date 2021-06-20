max_num = 4
price = [1500, 3000, 2000]
weight = [1, 4, 2]
cell = [[0 for i in range(0, max_num + 1)] for j in range(0, len(price) + 1)]
if __name__ == "__main__":
    for i in range(1, len(cell)):
        for j in range(1, len(cell[i])):
            if weight[i - 1] <= j:
                prev = j - weight[i - 1]
                current_price = price[i - 1]
                prev_price = cell[i - 1][j]
                previous_object_price = cell[i - 1][prev]
                cell[i][j] = max(current_price + previous_object_price, prev_price)
            else:
                cell[i][j] = cell[i - 1][j]
    print(cell[len(price)][max_num])
