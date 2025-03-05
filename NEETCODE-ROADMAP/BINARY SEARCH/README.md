# Binary Search Algorithm

Binary Search is an efficient algorithm used to find the position of a target value in a **sorted** array.

## Requirements
- The array **must** be sorted.
- Access to any element in the data structure should take **constant time**.

## Step-by-Step Explanation
1. Find the **middle** position of the array.
2. Compare the middle value with the **target value**.
3. If the middle value is **greater** than the target, update **right = middle - 1**.
4. If the middle value is **smaller** than the target, update **left = middle + 1**.
5. Repeat the process until the target is found or the search space is exhausted.

## Application of Binary Search
1. Find an element in sorted array
2. Searching in infinite list (Google Search Autocomplete)
3. Finding peak element in an array
4. Optimizing search space in problem lik **Minimum in rotated sorted array**

## Binary Search Code (Python) - Best for large data
```python
def binary_search(arr, target):
    if not arr:
        return -1  # Return -1 if the array is empty
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Return -1 if the target is not found
```
The iterative version of Binary Search is often be preferred, cause it avoids recursion overhead.

## Binary Search with Upper Bound (Next Greater Element)
```python
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

arr = [1, 2, 2, 4, 5]
print(upper_bound(arr, 2))  # Output: 3 (Index of 4)
```

## Binary Search with Recursive Approach
```python
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

# Recursive example
def recursive(n):
    if n == 1:
        return n
    return recursive(n-1)
```
This approach is elegant, but can be overflow for large input data

## Some articles to read
- [Wikipedia - Binary Search](https://en.wikipedia.org/wiki/Binary_search)
- [GeekforGeek - Binary Search](https://www.geeksforgeeks.org/binary-search/)
- [W3school - Binary Search](https://www.w3schools.com/dsa/dsa_algo_binarysearch.php)