s = "   fly me   to   the moon  "


def lengthOfLastWord(s):
    return len(s.strip().split(' ')[-1])


print(lengthOfLastWord(s))
