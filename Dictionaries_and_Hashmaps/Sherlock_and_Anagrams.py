def sherlock_and_anagrams(s):
    count = 0
    pattern_dict = dict()
    len_s = len(s)

    for i in range(len_s):
        for j in range(len_s - i):
            sub = ''.join(sorted(s[j:(j + i + 1)]))
            try:
                pattern_dict[sub] += 1
            except:
                pattern_dict[sub] = 1

    for i in pattern_dict:
        val = pattern_dict[i]
        count += val * (val - 1) // 2
    return count
