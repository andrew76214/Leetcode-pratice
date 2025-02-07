# 72 ms Beats 30.04%
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left_pointer, max_window_size, zero_count = 0, 0, 0

        for right_pointer in range(len(nums)):
            if (nums[right_pointer] == 0):
                zero_count += 1
            
            while (zero_count > k):
                if nums[left_pointer] == 0:
                    zero_count -= 1
                left_pointer += 1
            
            max_window_size = max(max_window_size, right_pointer - left_pointer + 1)

        return max_window_size


# TLE
# len(nums)找不到，就窮舉找len(nums)-1
# 邏輯對，但會超時
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_window_size = 0
        current_window_size = len(nums)

        while (current_window_size > max_window_size):
            for i in range(len(nums) - current_window_size + 1):
                if (nums[i:i+current_window_size].count(0) <= k):
                    max_window_size = current_window_size

            current_window_size -= 1
        
        return max_window_size
