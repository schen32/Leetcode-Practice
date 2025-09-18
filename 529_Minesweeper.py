class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]
        m, n = len(board), len(board[0])

        def count_mines(i, j):
            mines = 0
            for x, y in directions:
                ix, jy = i + x, j + y
                if 0 <= ix < m and 0 <= jy < n and board[ix][jy] == "M":
                    mines += 1
            return mines

        def dfs(i, j):
            if board[i][j] != "E":
                return

            mines = count_mines(i, j)
            if mines > 0:
                board[i][j] = str(mines)
            else:
                board[i][j] = "B"
                for x, y in directions:
                    ix, jy = i + x, j + y
                    if 0 <= ix < m and 0 <= jy < n:
                        dfs(ix, jy)

        i, j = click
        if board[i][j] == "M":
            board[i][j] = "X"
        else:
            dfs(i, j)
        return board