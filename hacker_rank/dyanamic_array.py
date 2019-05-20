def dynamicArray(n, queries):
    lastAnswer = 0
    result = []
    seqList = [[] for _ in range(n)]

    for query, x, y in queries:
        index = (x ^ lastAnswer) % n
        if (query == 1):
            seqList[index].append(y)
        else:
            lastAnswer = seqList[index][y % len(seqList[index])]
            # print(lastAnswer)
            result.append(lastAnswer)

    return result


dynamicArray(2, [
    [1, 0, 5],
    [1, 1, 7],
    [1, 0, 3],
    [2, 1, 0],
    [2, 1, 1],
])
