class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        
        left_ptr, right_ptr = 0, len(nums) - 1
        count = 0
        nums.sort()

        while left_ptr < right_ptr:
            if (nums[left_ptr] + nums[right_ptr]) < target:
                count += (right_ptr - left_ptr)
                left_ptr += 1
            else:
                right_ptr -= 1
            
        return count
