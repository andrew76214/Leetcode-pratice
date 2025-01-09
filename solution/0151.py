class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
         # 將字符串分割成單字列表，並移除空字串元素
        words = [word for word in s.split(' ') if word]
        
        # 將單字反轉並加入回字符串
        result = ' '.join(words[::-1])
        
        # print(result)
        return result
