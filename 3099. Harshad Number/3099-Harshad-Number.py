class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        totalChar = 0
        temp = x

        while temp != 0:
            totalChar += temp % 10
            temp //= 10
        
        if x % totalChar == 0:
            return totalChar
        
        return -1
        