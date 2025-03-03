class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            if (1 & n):  # AND邏輯運算
                ans += 1
            n >>= 1  # 往右Shift
        return ans
