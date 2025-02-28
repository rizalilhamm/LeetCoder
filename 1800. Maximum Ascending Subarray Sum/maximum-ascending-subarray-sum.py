class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = nums[0]
        res = curr

        for idx in range(1, len(nums)):
            if nums[idx-1] < nums[idx]:
                curr += nums[idx]
            else:
                curr = nums[idx]

            res = max(res, curr)

        return res