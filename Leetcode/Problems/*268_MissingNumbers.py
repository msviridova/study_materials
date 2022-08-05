nums = [0]


def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)):
        if i != nums[i]:
            return i
        elif i == nums[i] and i == nums[-1]:
            return i+1

print(missingNumber(nums))