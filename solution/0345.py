class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            # 移動左指針直到遇到元音
            while left < right and s_list[left] not in vowels:
                left += 1
            # 移動右指針直到遇到元音
            while left < right and s_list[right] not in vowels:
                right -= 1
            # 交換左邊和右邊的元音
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left, right = left + 1, right - 1

        # 將清單轉回字串
        return ''.join(s_list)
