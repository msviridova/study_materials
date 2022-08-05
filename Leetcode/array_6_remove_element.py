nums = [0,1,2,2,3,0,4,2]
val = 2


def removeElement(nums, val):
    for i in nums:
        if i == val:
            print(i)
            nums.remove(val)
            print(nums)
    return nums

print(removeElement(nums, val))