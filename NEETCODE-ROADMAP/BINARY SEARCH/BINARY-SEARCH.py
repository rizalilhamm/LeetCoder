# Best for large data
def binarySearch(arr, target):
    if len(arr) == 0:
        return 0
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return target
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# Recursively Approach
def binarySearch2(arr, left, right, target):
    if right < left:
        return -1
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return arr[mid]
    elif arr[mid] < target:
        return binarySearch2(arr, mid + 1, right, target)
    else:
        return binarySearch2(arr, mid - 1, right, target)

def recursive(n):
    if n == 1:
        return n
    return recursive(n-1)
            

arr = [1,2,3,4,5,6,7,8,9]
# print(binarySearch(arr,51))
# print(recursive(10))

print('result: ',binarySearch2(arr, 0, len(arr)-1, 7))
print('result: ',binarySearch2(arr, 0, len(arr)-1, 100))
            
        
    