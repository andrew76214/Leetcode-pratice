class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}  # 紀錄每顆球的顏色
        color_count = {}  # 紀錄每種顏色的出現次數
        distinct_colors = set()  # 追蹤當前不同的顏色
        result = []

        for x, y in queries:
            if x in ball_color:
                old_color = ball_color[x]
                color_count[old_color] -= 1  # 減少舊顏色的計數
                if color_count[old_color] == 0:
                    distinct_colors.remove(old_color)  # 若舊顏色數量歸零，從 Set 移除
            
            # 更新新顏色
            ball_color[x] = y
            if y not in color_count:
                color_count[y] = 0
            color_count[y] += 1

            distinct_colors.add(y)  # 新顏色一定要在 Set 中
            result.append(len(distinct_colors))  # 記錄當前不同顏色的數量

        return result
