class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1
        
        # Compute prefix sum
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        total_sum = prefix_sum[-1]  # Total sum of array
        
        # Find the pivot index
        for j in range(len(nums)):
            left_sum = prefix_sum[j] - nums[j]  # Sum of elements before index j
            right_sum = total_sum - prefix_sum[j]  # Sum of elements after index j
            
            if left_sum == right_sum:
                return j  # Return the index
        
        return -1  # Return -1 if no pivot index is found
