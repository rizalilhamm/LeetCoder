# https://leetcode.com/problems/partition-array-according-to-given-pivot
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, middle, right = [], [], []
        for num in nums:
            if num == pivot:
                middle.append(num)
            elif num < pivot:
                left.append(num)
            else:
                right.append(num)

        return left + middle + right