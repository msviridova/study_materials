nums = [222,151,842,244,103,736,219,432,565,216,
        36,198,10,367,778,111,307,460,92,622,
        750,36,559,983,782,432,312,111,676,179,
        44,86,766,371,746,905,850,170,892,80,
        449,932,295,875,259,556,730,441,153,869]
key = 153
k = 19


class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        ans = set()
        for i, num in enumerate(nums):
            if num == key:
                ans.update(range(max(0, i - k), min(i + k + 1, len(nums))))
        return list(ans)

o = Solution()

print(o.findKDistantIndices(nums, key, k))