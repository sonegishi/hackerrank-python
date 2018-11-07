def array_manipulation(n, queries):
    arr = [0 for _ in range(n + 1)]
    for [lower, upper, val] in queries:
        arr[lower - 1] += val
        arr[upper] -= val

    max = 0
    sum = 0
    for e in arr:
        sum += e
        if sum > max:
            max = sum
    return max
