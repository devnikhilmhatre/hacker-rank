def jumpingOnClouds(c):
    jumps = 0
    step = 1
    length = len(c)
    con = False

    while step < length:
        if con:
            con = False
            step += 1
            continue
        next_step = step + 1
        if next_step < length:
            if c[next_step] == 0:
                jumps += 1
                con = True
            elif c[step] == 0:
                jumps += 1
        else:
            jumps += 1
        step += 1
    return jumps


arr = [0, 0, 0, 0, 1, 0]
# arr = [0, 0, 1, 0, 0, 1, 0]
# arr = [0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(arr))
