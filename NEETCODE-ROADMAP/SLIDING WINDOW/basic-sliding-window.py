print("hello, world")

# We use a Python interpreter that's compiled to Web Assembly
# to run code right in your browser using a web worker
def getMaxSum(arr, k):
    maxSum = 0
    windowSum = 0
    start = 0
    
    for i in range(len(arr)):
        windowSum += arr[i]
        if ((i - start + 1) == k):
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[start]
            start += 1
    
    return maxSum


print(getMaxSum([3, 5, 2, 1, 7], 2))