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


arr = [1,2,3,4,5,6,7,8,9]
print(binarySearch(arr,51))
            
        
    