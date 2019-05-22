def sockMerchant(n, ar):
    pairs = 0
    for i in set(ar):
        count = ar.count(i)
        if count % 2 == 0:
            pairs += count / 2
        else:
            count -= 1
            pairs += count / 2

    return pairs


sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])