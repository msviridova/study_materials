def romanToInt(s):
    result = 0
    for i in range(len(s)):
        if s[i] == 'M':
            if i == 0 or s[i-1] != 'C':
                result += 1000
            else:
                continue
        elif s[i] == 'D':
            if s[i-1] == 'C' and i != 0:
                continue
            result += 500
        elif s[i] == 'C':
            if s[i-1] == 'X' and i != 0:
                continue
            elif i == len(s) - 1:
                result += 100
            elif s[i+1] == 'D':
                result += 400
            elif s[i+1] == 'M':
                result += 900
            else:
                result += 100
        elif s[i] == 'L':
            if s[i - 1] == 'X' and i != 0:
                continue
            else:
                result += 50
        elif s[i] == 'X':
            if s[i - 1] == 'I' and i != 0:
                continue
            elif i == len(s)-1:
                result += 10
            elif s[i+1] == 'L':
                result += 40
            elif s[i + 1] == 'C':
                result += 90
            else:
                result += 10
        elif s[i] == 'V':
            if s[i - 1] == 'I' and i != 0:
                continue
            else:
                result += 5
        elif s[i] == 'I':
            if i == len(s)-1:
                result += 1
            elif s[i + 1] == 'V':
                result += 4
            elif s[i + 1] == 'X':
                result += 9
            else:
                result += 1

    return result
