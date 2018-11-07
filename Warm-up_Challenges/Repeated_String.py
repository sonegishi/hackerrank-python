def repeated_string(s, n):
    len_s = len(s)
    counts = n // len_s * a_counter(s) + a_counter(s[:(n % len_s)])
    return counts


def a_counter(string):
    counter = 0
    for x in string:
        if x == 'a':
            counter += 1
    return counter
