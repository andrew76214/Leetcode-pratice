class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        N=len(grid)
        d=defaultdict(int)
        ans=0
        
        for row in grid:
            t=tuple(row)
            d[t]+=1
            
        for c in range(N):
            col=[grid[r][c] for r in range(N)]
            t=tuple(col)
            ans+=d[t]
            
        return ans
