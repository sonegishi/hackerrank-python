def counting_valleys(n, s):
    curr_level = 0
    counter = 0

    for step in s:
        if step == 'U':
            curr_level += 1
        else:
            if 0 <= curr_level < 1:
                counter += 1
            curr_level -= 1

    return counter
