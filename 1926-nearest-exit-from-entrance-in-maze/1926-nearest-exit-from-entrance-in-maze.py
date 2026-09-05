from collections import deque

class Solution:

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        dirs = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        rows = len(maze)
        cols = len(maze[0])

        visited = [[False] * cols for _ in range(rows)]

        queue = deque([
            (entrance[0], entrance[1], 0)
        ])

        visited[entrance[0]][entrance[1]] = True

        while queue:

            row, col, step = queue.popleft()

            for dr, dc in dirs:

                next_row = row + dr
                next_col = col + dc

                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue

                if visited[next_row][next_col]:
                    continue

                if maze[next_row][next_col] != ".":
                    continue

                # 출구
                if (
                    next_row == 0
                    or next_row == rows - 1
                    or next_col == 0
                    or next_col == cols - 1
                ):
                    return step + 1

                visited[next_row][next_col] = True
                queue.append(
                    (next_row, next_col, step + 1)
                )

        return -1