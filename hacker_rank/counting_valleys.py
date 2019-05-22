def countingValleys(n, s):
    step = 0
    valley = 0

    for i in s:

        if step == 0:
            start = i

        if i == 'U':
            step += 1
        else:
            step -= 1

        if step == 0 and start == 'D':
            valley += 1

    return valley


# string = 'DDUUDDUDUUUD'
string = 'UDUUUDUDDD'
# string = 'UDDDUDUU'

print(countingValleys(8, string))
