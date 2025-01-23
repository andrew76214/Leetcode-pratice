class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        for i in range(len(t)):
            if s != "" and t[i] == s[count]:
                count += 1
                if count == len(s):
                    return True
            
        if count == len(s):
            return True
        else:
            return False
