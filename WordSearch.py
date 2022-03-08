class Solution:
    def exist(self, board, word: str) -> bool:
        """
        Backtracking
        """
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(row, col, current_idx): 
            if current_idx == len(word):
                return True

            if row<0 or col<0 or row>=rows or col>=cols or board[row][col] != word[current_idx] or (row, col) in visited:     
                return False

            visited.add((row, col)) # in this iteration of backtrack, we won't need to visited this cell again

            # call dfs on each neighbor of current cell
            res = dfs(row+1, col, current_idx+1) or dfs(row-1, col, current_idx+1) or dfs(row, col+1, current_idx+1) or dfs(row, col-1, current_idx+1)
            
            visited.remove((row, col)) # So that this does obstruct other dfs calls
            
            return res


        for row in range(rows):
            for col in range(cols):
                res = dfs(row, col, 0)
                if res:
                    return True
        return False