class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
 
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
 
    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)
 
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))
 
edges = []
print("Enter edges as: source destination weight")
for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
 
adj = [[] for i in range(n)]
for w, u, v in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))
 
edges.sort()
dsu = DSU(n)
total = 0
count = 0
 
print("Selected edges:")
for w, u, v in edges:
    if dsu.find(u) != dsu.find(v):
        dsu.union(u, v)
        print(u, "-", v, ":", w)
        total += w
        count += 1
 
if count == n - 1:
    print("Total weight:", total)
else:
    print("Graph is disconnected; MST does not exist")
