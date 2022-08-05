arr = [0,4,1,0,0,8,0,0,3]


# мое решение
# def duplicateZeros(arr):
#     index = 0
#     for i in range(len(arr)):
#         if index == 1:
#             index = 0
#             continue
#         elif arr[i] != 0:
#         else:
#             arr.insert(i+1, 0)
#             arr.pop()
#             index = 1

# лучшее решение
def duplicateZeros(arr):
    s = 0
    d = 0

    destination = []

    # Copy is performed until the destination array is full.
    for s in range(len(arr)):
        if arr[s] == 0:
            # Copy zero twice.
            destination[d] = 0
            d += 1
            destination[d] = 0
        else:
            destination[d] = arr[s]

        d += 1

print(duplicateZeros(arr))