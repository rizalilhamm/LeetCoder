class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        resMap = {}
        tempNums = nums1 + nums2
        for idx in range(len(tempNums)):
            if tempNums[idx][0] not in resMap:
                resMap[tempNums[idx][0]] = tempNums[idx][1]
            else:
                resMap[tempNums[idx][0]] += tempNums[idx][1]
        
        keys = []
        for key in resMap.keys():
            keys.append(key)
        
        keys.sort()
        result = []
        for key in keys:
            res = [key, resMap[key]]
            result.append(res)

        return result