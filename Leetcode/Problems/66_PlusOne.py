digits = [1, 2, 3]


def plusOne(digits):
    result = int("".join([str(n) for n in digits])) + 1
    return [int(x) for x in str(result)]

print(plusOne(digits))