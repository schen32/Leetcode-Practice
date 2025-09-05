class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            col_set = set()
            box_set = set()

            for j in range(9):
                # Row check
                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])

                # Column check
                if board[j][i] != ".":
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])

                # Box check
                row_idx = 3 * (i // 3) + j // 3
                col_idx = 3 * (i % 3) + j % 3
                if board[row_idx][col_idx] != ".":
                    if board[row_idx][col_idx] in box_set:
                        return False
                    box_set.add(board[row_idx][col_idx])

        return True
