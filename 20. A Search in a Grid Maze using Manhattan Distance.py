
import heapq

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

def heuristic(a):
    return abs(a[0] - goal[0]) + abs(a[1] - goal[1])

queue = [(heuristic(start), 0, start)]
parent = {start: None}
cost = {start: 0}

while queue:
    f, g, current = heapq.heappop(queue)

    if current == goal:
        break

    r, c = current

    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < 5 and 0 <= nc < 5 and grid[nr][nc] == 0:

            new_cost = g + 1

            if (nr, nc) not in cost or new_cost < cost[(nr, nc)]:
                cost[(nr, nc)] = new_cost
                parent[(nr, nc)] = current

                f = new_cost + heuristic((nr, nc))
                heapq.heappush(queue, (f, new_cost, (nr, nc)))

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
