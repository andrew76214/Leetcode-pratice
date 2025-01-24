class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Sorting
        nums.sort()

        # Count
        left_index = 0
        right_index = len(nums) - 1
        count = 0

        while left_index < right_index:
            if (nums[left_index] + nums[right_index]) == k:
                count += 1
                left_index += 1
                right_index -= 1
            elif((nums[left_index] + nums[right_index]) < k):
                left_index += 1
            else:
                right_index -= 1
            
        return count
