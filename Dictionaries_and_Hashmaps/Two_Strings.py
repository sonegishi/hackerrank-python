def two_strings(s1, s2):
    char_dict = {char: True for char in s1}

    for char in s2:
        if char in char_dict:
            return 'YES'
    return 'NO'
