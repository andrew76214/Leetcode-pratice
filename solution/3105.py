class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # initial
        inc = dec = 1
        ans = 0
        if (len(nums) == 1):
            return 1
        elif nums == None:
            return 0
        
        # counting
        for i in range(1, len(nums)):
            if (nums[i] > nums[i-1]):
                inc += 1
                dec = 1
                print('inc')
            elif (nums[i] < nums[i-1]):
                inc = 1
                dec += 1
                print('dec')
            else:
                inc = dec = 1
            
            ans = max(ans, inc, dec)

        return ans
