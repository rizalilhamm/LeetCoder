class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        res, idx = 0, 0
        
        while res < n:
            res = 3 ** idx
            if res == n:
                return True
            idx += 1

        return False