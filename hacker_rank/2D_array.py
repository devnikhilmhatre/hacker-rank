# matrix = [
#     [1, 1, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0],
#     [0, 0, 2, 4, 4, 0],
#     [0, 0, 0, 2, 0, 0],
#     [0, 0, 1, 2, 4, 0],
# ]

matrix = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]


def generate_hour_glasses(arr):
    height = len(arr)
    width = len(arr[0])
    hour_glass_sum_list = []

    # print(f'Matrix: ({height} x {width})')

    for i in range(height - 2):  # row

        # columns
        start = 0
        end = 3

        run = True
        while run:
            hour_glass = []
            # Top
            for j in range(start, end):
                hour_glass.append((i, j))

            # Middle
            hour_glass.append((i + 1, start + 1))

            # Bottom

            for k in range(start, end):
                hour_glass.append((i + 2, k))

            start += 1
            end += 1
            # hour_glasses.append(hour_glass)
            print(hour_glass)
            val = 0
            for first, second in hour_glass:
                val += arr[first][second]
            hour_glass_sum_list.append(val)
            if end == width + 1:
                run = False

    return max(hour_glass_sum_list)


print(generate_hour_glasses(matrix))
