class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        row , col = len(board), len(board[0])
        
        directions = [(-1,-1), (-1,0),(-1,1),
                      (0,-1),        (0,1),
                       (1,-1), (1,0), (1,1)]
        for r in range(row):
            for c in range(col):
                
                live_neighbors = 0
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    
                    if 0<=nr<row and 0<= nc < col and abs(board[nr][nc])==1:
                        live_neighbors+=1
                        
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1  # Mark as dead (was live)
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2  # Mark as live (was dead)
                    
                    
        for r in range(row):
            for c in range(col):
                if board[r][c]==-1:
                    board[r][c]=0
                    
                if board[r][c]==2:
                    board[r][c] = 1
                        
                        
        