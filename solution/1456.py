class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        sub_string = s[:k]  # 取出前 k 個字母作為初始子字串
        count_vowel = sum(1 for c in sub_string if c in 'aeiou')  # 計算初始母音數量
        max_vowel = count_vowel

        for i in range(len(s) - k):
            # 檢查移出的字母是否是母音
            if s[i] in 'aeiou':
                count_vowel -= 1

            # 檢查新加入的字母是否是母音
            if s[i + k] in 'aeiou':
                count_vowel += 1

            max_vowel = max(max_vowel, count_vowel)

            # print('sub_string = ', s[i + 1:i + k + 1])  # 子字串輸出

        return max_vowel
