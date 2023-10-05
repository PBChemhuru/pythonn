from numpy import random


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int(((high + low) / 2))
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


num = random.randint(100, size=7)
print(num)
s = 45
result = binary_search(num, s)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

