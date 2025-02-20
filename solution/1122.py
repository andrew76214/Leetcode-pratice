class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 計算 arr1 中每個數字的出現次數
        count_map = Counter(arr1)
        
        # 根據 arr2 順序排列
        result = []
        for num in arr2:
            result.extend([num] * count_map.pop(num, 0))  # 取出 num 的個數並加入結果
        
        # 處理 arr2 沒有的數字，按數字大小排序
        remaining = sorted(count_map.elements())  # `elements()` 會展開 Counter 內的值
        
        return result + remaining
