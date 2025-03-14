# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

def is_valid_minesweeper(n, m, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    def count_bombs(x, y):
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '*':
                count += 1
        return count

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                if count_bombs(i, j) > 0:
                    return "NO"
            elif grid[i][j] not in '*':
                if int(grid[i][j]) != count_bombs(i, j):
                    return "NO"

    return "YES"

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
print(is_valid_minesweeper(n, m, grid))
