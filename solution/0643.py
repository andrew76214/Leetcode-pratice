class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum_sum = 0
        tmp_sum = 0
        for i in range(k):
            maximum_sum += nums[i]

        tmp_sum = maximum_sum

        for j in range(1, len(nums) - k + 1):
            tmp_sum -= nums[j-1]
            tmp_sum += nums[j-1+k]
            
            if tmp_sum > maximum_sum:
                maximum_sum = tmp_sum
        
        return (maximum_sum / k)
