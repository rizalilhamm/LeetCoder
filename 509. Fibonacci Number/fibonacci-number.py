class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prev, curr = 0, 1

        for idx in range(2, n+ 1) :
            temp = curr
            curr = curr + prev
            prev = temp

        return curr