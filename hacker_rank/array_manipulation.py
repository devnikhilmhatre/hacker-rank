# case 1
length = 5
queries = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100],
]

# case 2
# length = 10
# queries = [
#     [1, 5, 3],
#     [4, 8, 7],
#     [6, 9, 1],
# ]

# case 3

# length = 10

# queries = [
#     [2, 6, 8],
#     [3, 5, 7],
#     [1, 8, 1],
#     [5, 9, 15],
# ]


def arrayManipulation(n, queries):
    arr = [0] * (n + 2)
    print(arr)
    for start, end, value in queries:
        arr[start] += value
        arr[end + 1] -= value
        # print(arr)
        # for i in range(start - 1, end):
        # arr[i] += value
    _max = x = 0
    for i in arr:
        x += i
        if _max < x:
            _max = x

    return _max


print(arrayManipulation(length, queries))
