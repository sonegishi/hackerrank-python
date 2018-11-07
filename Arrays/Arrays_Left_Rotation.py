def rot_left(a, d):
    len_a = len(a)
    if d >= len_a:
        d = d % len_a
    return a[d:len_a] + a[0:d]
