import time
queries = [
    (1, 1),
    (2, 2),
    (3, 2),
    (1, 1),
    (1, 1),
    (2, 1),
    (3, 2),
]


def freqQuery(queries):
    d = {}
    ar = []
    append = ar.append
    # values = []
    for query, data in queries:
        if query == 1:
            # key = data
            # current = d.get(key, 0)
            # new = current + 1
            # d[key] = new
            # values.add(new)

            if data in d:
                d[data] += 1
            else:
                d[data] = 1

        elif query == 2:
            # key = data
            # current = d.get(key, 0)
            # new = current - 1
            # d[key] = new
            # if new > 0:
            #     values.add(new)

            if data in d:
                _d = d[data] - 1
                if _d < 0:
                    del d[data]
                else:
                    d[data] = _d
        else:
            if data in d.values():
                append(1)
            else:
                append(0)
        # print(d)
    return ar


with open('hacker_rank/input_freq_query.txt', 'r') as f:
    arr = []
    for i in range(int(f.readline())):
        arr.append(tuple(int(i) for i in f.readline().rstrip().split(' ')))
        # print(arr)
    start = time.time()
    abc = freqQuery(arr)
    # abc = freqQuery(queries)
    end = time.time()
    print(end - start)
    # print(abc)

    with open('hacker_rank/output_freq_query.txt', 'r') as fi:
        _rr = []
        try:
            for i in range(33246):
                d = fi.readline()
                if d != '':
                    _rr.append(int(d))
                # print(d)
        except Exception as identifier:
            print(identifier)
        t = 0
        for i, (a, b) in enumerate(zip(_rr, abc)):
            if (a == b) is False:
                # print(i)
                t += 1
        print(t)
