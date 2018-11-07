def minimum_swaps(arr):
    len_arr = len(arr)
    # Make a list of tuples which contains initial position and its value
    pos_val_arr = [*enumerate(arr)]
    # Sort the list based on the values
    pos_val_arr.sort(key=lambda x: x[1])
    # Make a boolean dictionary to check ...
    cycle_dict = {key: False for key in range(len_arr)}

    swap_counter = 0
    for i in range(len_arr):
        # Find a number of elements involved in one cycle based on the init. pos.
        cycle_size = 0
        init_pos = i
        while not cycle_dict[init_pos]:
            cycle_dict[init_pos] = True
            init_pos = pos_val_arr[init_pos][0]
            cycle_size += 1

        if cycle_size > 0:
            swap_counter += (cycle_size - 1)

    return swap_counter
