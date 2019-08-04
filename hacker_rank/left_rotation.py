arr = [1, 2, 3, 4, 5]


def rotate_left(arr, length_of_arr, rotation_num):

    new_arr = [arr[i] for i in range(rotation_num, length_of_arr)]

    for i in range(rotation_num):
        new_arr.append(arr[i])

    for i in new_arr:
        print(i, end=" ")


rotate_left(arr, 5, 4)
