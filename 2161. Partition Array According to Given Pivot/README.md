## LeetCode Question: Partition Array According to Given Pivot

**Problem Link**: [Partition Array According to Given Pivot](https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=daily-question&envId=2025-03-03)

### Problem Description:

You are given an integer array `nums` and an integer `pivot`. You need to partition the array into two parts:

- All elements that are less than `pivot` should come before the pivot.
- All elements that are greater than `pivot` should come after the pivot.
- The relative order of elements within each part should be preserved.

Return the partitioned array.

**Example**:

Input: `nums = [9, 12, 5, 10, 14, 3, 10], pivot = 10`

Output: `[9, 5, 3, 10, 14, 10, 12]`

---

### Constraints:
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 10^6`
- `1 <= pivot <= 10^6`

---

**Note**:
- The problem should be solved in O(n) time complexity, where n is the length of the array.
