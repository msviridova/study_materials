nums = [-4,-1,0,3,10]


def sortedSquares(nums):
    s = [x * x for x in nums]
    return sorted(s)

print(sortedSquares(nums))

