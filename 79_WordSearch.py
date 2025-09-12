class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        m = len(board)
        n = len(board[0])

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def backtrack(row, col, i, visited):
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= m or col >= n:
                return False
            if board[row][col] != word[i]:
                return False
            if (row, col) in visited:
                return False
            visited.add((row, col))

            for x, y in directions:
                if backtrack(row + x, col + y, i + 1, visited):
                    return True

            visited.remove((row, col))
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0, set()):
                        return True
        return False