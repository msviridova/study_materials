nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


#мое решение
def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1.pop()

    for i in nums2:
        nums1.append(i)

    nums1.sort()
    return nums1

#лучшее решение
def merge(nums1, m, nums2, n):
    full = []
    full.extend(nums1[:m])
    full.extend(nums2)
    full.sort()
    for i in range(len(nums1)):
        nums1[i] = full[i]


print(merge(nums1, m, nums2, n))