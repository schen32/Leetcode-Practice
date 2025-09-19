class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        m = len(board)
        rook_row, rook_col = 0, 0
        for i in range(m):
            for j in range(m):
                if board[i][j] == "R":
                    rook_row = i
                    rook_col = j
                    break

        left, right = rook_col - 1, rook_col + 1
        top, bottom = rook_row - 1, rook_row + 1
        captures = 0
        while left >= 0:
            if board[rook_row][left] == "B":
                break
            elif board[rook_row][left] == "p":
                captures += 1
                break
            left -= 1
        while right < m:
            if board[rook_row][right] == "B":
                break
            elif board[rook_row][right] == "p":
                captures += 1
                break
            right += 1
        while top >= 0:
            if board[top][rook_col] == "B":
                break
            elif board[top][rook_col] == "p":
                captures += 1
                break
            top -= 1
        while bottom < m:
            if board[bottom][rook_col] == "B":
                break
            elif board[bottom][rook_col] == "p":
                captures += 1
                break
            bottom += 1
        return captures