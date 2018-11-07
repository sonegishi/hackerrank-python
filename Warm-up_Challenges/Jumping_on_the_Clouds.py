def jumping_on_the_clouds(c):
    stack = list()
    jumps = 0

    for cloud in c:
        if cloud == 0:
            stack.append(cloud)
            if len(stack) == 2:
                jumps += 1
                del stack[:]
        else:
            jumps += 1
            if len(stack) > 1:
                jumps += 1
            del stack[:]

    return jumps + 1 if len(stack) > 1 else jumps
