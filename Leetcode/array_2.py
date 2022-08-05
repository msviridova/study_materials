nums = [555,901,482,1771]

def findNumbers(nums):
    result = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            result += 1
    return result

print(findNumbers(nums))