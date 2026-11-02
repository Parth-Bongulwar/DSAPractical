
from collections import deque

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

queue = deque([start])
visited = [start]
parent = {start: None}

while queue:
    r, c = queue.popleft()

    if (r, c) == goal:
        break

    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < 5 and 0 <= nc < 5:
            if grid[nr][nc] == 0 and (nr, nc) not in visited:

                visited.append((nr, nc))
                parent[(nr, nc)] = (r, c)
                queue.append((nr, nc))

if goal in parent:
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    print("Shortest path:", path)
else:
    print("No path exists")
