n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix (0 for no edge):")
 
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
 
selected = [False] * n
selected[0] = True
total = 0
 
print("Selected edges:")
for step in range(n - 1):
    minimum = float("inf")
    u = -1
    v = -1
 
    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        u = i
                        v = j
 
    if u == -1:
        print("Graph is disconnected")
        break
 
    print(u, "-", v, ":", minimum)
    total += minimum
    selected[v] = True
 
if all(selected):
    print("Total weight:", total)
