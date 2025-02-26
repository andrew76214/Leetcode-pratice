class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        count = start
        for i in range(1, n):
            count ^= (start + (2*i))

        return count
