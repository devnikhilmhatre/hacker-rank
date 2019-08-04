def repeatedString(s, n):
    base_count = s.count('a')
    quotient = n // len(s)
    remainder = n % len(s)
    return (base_count * quotient) + s[:remainder].count('a')


print(repeatedString('aba', 10))
