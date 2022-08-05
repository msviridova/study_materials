nums = [1,1,0,1,1,1]


# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         max_1 = 0
#         result = 0
#         for i in nums:
#             if i == 1:
#                 max_1 +=1
#             else:
#                 if max_1 > result:
#                     result = max_1
#                     max_1 = 0
#                 else:
#                     continue
#         return result


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        result = []
        row = []
        for i in nums:
            if i == 1:
                row.append(i)
            else:
                result.append(row)
                row = []
            result.append(row)
        return len(max(result, key=len))


