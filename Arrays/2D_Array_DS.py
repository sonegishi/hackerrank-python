def hourglass_sum(arr):
    num_rows = len(arr)
    num_cols = len(arr[0])

    sums = list()
    col_idx = 0
    while col_idx + 2 < num_cols:
        row_idx = 0
        while row_idx + 2 < num_rows:
            sums.append(sum(arr[row_idx][col_idx:col_idx + 3]
                            + arr[row_idx + 2][col_idx:col_idx + 3])
                        + arr[row_idx + 1][col_idx + 1])
            row_idx += 1
        col_idx += 1

    return max(sums)
