class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        
        # 計算每個字符的頻率
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # 遍歷字串，找到第一個出現一次的字符
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        
        return -1
