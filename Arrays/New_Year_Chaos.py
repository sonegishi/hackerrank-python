def minimum_bribes(q):
    bribes = 0
    for i in range(len(q)):
        if q[i] - i > 3:
            return 'Too chaotic'
        for k in range(max(0, q[i]-2), i):
            if q[k] > q[i]:
                bribes += 1
    return bribes
