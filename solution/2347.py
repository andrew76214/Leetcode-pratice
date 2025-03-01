from typing import List

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # 如果所有花色相同，則是 Flush
        if len(set(suits)) == 1:
            return 'Flush'

        # 計算 rank 的頻率
        freq = {}
        for r in ranks:
            freq[r] = freq.get(r, 0) + 1

        # 取得最大頻率
        max_freq = max(freq.values())

        if max_freq >= 3:
            return 'Three of a Kind'
        elif max_freq == 2:
            return 'Pair'
        else:
            return 'High Card'
