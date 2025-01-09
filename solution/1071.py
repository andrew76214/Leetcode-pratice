class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        if (str1 + str2) != (str2 + str1):
            return ''

        def gcd(x, y):
            if (y == 0):
                return x
            else:
                return gcd(y, x%y)
            
        return (str1[:gcd(len(str1), len(str2))])
