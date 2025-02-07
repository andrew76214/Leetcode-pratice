class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left_pointer, max_window_size, zero_count = 0, 0, 0

        for right_pointer in range(len(nums)):
            if (nums[right_pointer] == 0):
                zero_count += 1
            
            while (zero_count > 1):
                if (nums[left_pointer] == 0):
                    zero_count -= 1
                left_pointer += 1
            
            max_window_size = max(max_window_size, right_pointer - left_pointer)

        return max_window_size
