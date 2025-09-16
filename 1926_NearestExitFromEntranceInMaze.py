class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(0, entrance[0], entrance[1])])
        visited = {(entrance[0], entrance[1])}

        m = len(maze)
        n = len(maze[0])
        while queue:
            steps, row, col = queue.popleft()
            if (row == 0 or row == m - 1 or col == n - 1 or col == 0) and (row, col) != tuple(entrance):
                return steps

            for x, y in directions:
                next_row, next_col = row + x, col + y
                if not next_row in range(m) or not next_col in range(n):
                    continue
                if not (next_row, next_col) in visited and maze[next_row][next_col] == ".":
                    visited.add((next_row, next_col))
                    queue.append((steps + 1, next_row, next_col))
        return -1