def mostFrequent(nums, key):
    dict = {}

    if len(nums) == 2:
        print(nums)
        if nums[0] != nums[1]:
            print(nums[0], nums[1])
            nums.remove(key)
            return nums[0]
        else:
            return nums[0]
    else:
        target = []
        for i in range(len(nums)):
            if nums[i] == key and i != len(nums) - 1:
                target.append(nums[i + 1])
        for n in target:
            dict[n] = target.count(n)
        return max(dict, key=dict.get)