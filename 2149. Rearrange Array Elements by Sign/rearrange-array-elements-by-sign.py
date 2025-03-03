class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posNums = []
        negNums = []

        for num in nums:
            if num < 0:
                negNums.append(num)
            else:
                posNums.append(num)

        result = []

        for idx in range(len(posNums)):
            result.append(posNums[idx])
            result.append(negNums[idx])
        
        return result