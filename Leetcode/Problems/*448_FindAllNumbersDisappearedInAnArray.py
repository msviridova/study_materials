nums = [4,3,2,7,8,2,3,1]

#мое решение
def findDisappearedNumbers(nums):
    result = []
    d = dict.fromkeys(nums)

    for i in range(len(nums)):
        if i + 1 not in d:
            result.append(i + 1)

    return result

#лучшее решение
print(set(range(1, len(nums)+1)) - set(nums))