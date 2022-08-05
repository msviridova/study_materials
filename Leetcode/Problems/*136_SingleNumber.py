nums = [2,2,1]

#мое решение
def singleNumber(self, nums):
    for i in set(nums):
        if nums.count(i) == 1:
            return i


#лучшее решение
def singleNumber(self, nums):
    return 2*sum(set(nums))-sum(nums)



print(sum(nums))