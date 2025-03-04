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

## Binary Search Code (Python)
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

## Some articles to read
- **Wikipedia - Binary Search** [Wikipedia - Binary Search](https://en.wikipedia.org/wiki/Binary_search)
- **GeekforGeek - Binary Search** [GeekforGeek - Binary Search](https://www.geeksforgeeks.org/binary-search/)
- **W3school - Binary Search** [W3school - Binary Search](https://www.w3schools.com/dsa/dsa_algo_binarysearch.php)