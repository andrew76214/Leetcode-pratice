class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 兩個字串的字母種類必須相同
        if set(word1) != set(word2):
            return False
        
        # 計算每個字母出現的次數
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # 轉換成排序後的頻率列表來比較
        return sorted(freq1.values()) == sorted(freq2.values())
