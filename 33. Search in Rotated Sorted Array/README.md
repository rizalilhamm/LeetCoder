# Search in Rotated Sorted Array

## Problem Description

You are given a **rotated sorted array** `nums` and an integer `target`. Your task is to determine the index of `target` in `nums`. If `target` is not present in `nums`, return `-1`.

A **rotated sorted array** is an array that has been sorted in ascending order and then rotated at some pivot unknown to you beforehand. For example, the array `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]` after rotation.

**Example 1:**
Input: nums = [4,5,6,7,0,1,2], target = 0 Output: 4

**Example 2:**
Input: nums = [4,5,6,7,0,1,2], target = 3 Output: -1

**Example 3:**
Input: nums = [1], target = 0 Output: -1


**Constraints:**
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is guaranteed to be rotated at some pivot.
- `-10^4 <= target <= 10^4`

**Note:** Your solution's runtime complexity must be in the order of O(log n).

For more details, refer to the [LeetCode problem description](https://leetcode.com/problems/search-in-rotated-sorted-array/).
