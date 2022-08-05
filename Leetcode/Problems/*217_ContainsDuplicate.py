nums = [3,1]


def containsDuplicate(nums):
    return len(nums) != len(set(nums))


print(containsDuplicate(nums))