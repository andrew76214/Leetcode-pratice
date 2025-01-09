class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def product_except_self(nums):
            n = len(nums)
            # Initialize the output array
            output = [1] * len(nums)
            
            # Compute prefix product for each element
            prefix = 1
            for i in range(n):
                output[i] = prefix
                prefix *= nums[i]
            
            # Compute suffix product for each element and multiply it with the prefix product
            suffix = 1
            for i in range(n - 1, -1, -1):
                output[i] *= suffix
                suffix *= nums[i]
            
            return output

        return product_except_self(nums)
