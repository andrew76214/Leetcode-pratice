class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []  # 用於儲存使用梯子的最大高度差
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:  # 需要爬升
                heapq.heappush(heap, diff)  # 先使用梯子策略
                
                if len(heap) > ladders:  # 當超過梯子數量時，使用磚塊
                    bricks -= heapq.heappop(heap)
                    
                if bricks < 0:  # 磚塊不夠時返回
                    return i

        return len(heights) - 1  # 能走完整個列表
