def sock_merchant(n, ar):
    socks_dict = dict()

    for sock in ar:
        if sock not in socks_dict:
            socks_dict[sock] = 1
        else:
            socks_dict[sock] += 1

    counter = 0
    for _, val in socks_dict.items():
        counter += val // 2

    return counter
