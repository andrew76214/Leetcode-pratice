class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 初始化追蹤的最小值和次小值
        first = float('inf')  # 第一個最小值
        second = float('inf') # 第二個最小值

        # 遍歷陣列
        for n in nums:
            if n <= first:  # 如果找到更小的數，更新 first
                first = n
            elif n <= second:  # 如果找到介於 first 和 second 的數，更新 second
                second = n
            else:  # 如果找到比 second 還大的數，說明存在遞增三元組
                return True
        
        return False  # 如果遍歷完都沒找到，返回 False
