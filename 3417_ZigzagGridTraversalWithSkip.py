class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = []
        skip = False  # used to skip alternate cells globally

        for i in range(m):
            # Determine traversal direction
            if i % 2 == 0:
                cols = range(n)         # left → right
            else:
                cols = range(n - 1, -1, -1)  # right → left

            for j in cols:
                if not skip:
                    res.append(grid[i][j])
                skip = not skip  # flip skip flag globally

        return res
