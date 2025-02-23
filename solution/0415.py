class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p_num1, p_num2 = len(num1) - 1, len(num2) - 1
        result_list = []
        carry = 0  # 使用整數來表示進位
        
        while p_num1 >= 0 or p_num2 >= 0 or carry:
            digit1 = int(num1[p_num1]) if p_num1 >= 0 else 0
            digit2 = int(num2[p_num2]) if p_num2 >= 0 else 0
            
            sum_ = digit1 + digit2 + carry
            carry = sum_ // 10  # 進位
            result_list.append(str(sum_ % 10))  # 取個位數存入
            
            p_num1 -= 1
            p_num2 -= 1
        
        return ''.join(result_list[::-1])  # 反轉 list 並轉成字串
