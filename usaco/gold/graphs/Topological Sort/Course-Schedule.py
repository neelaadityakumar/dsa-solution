from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)

in_degree = [0 for _ in range(n)]
for nodes in graph:
    for node in nodes:
        in_degree[node] += 1

queue = deque([i for i, in_deg in enumerate(in_degree) if in_deg == 0])
top_sort = []
while queue:
    curr = queue.popleft()
    top_sort.append(curr)
    for next_ in graph[curr]:
        in_degree[next_] -= 1
        if in_degree[next_] == 0:
            queue.append(next_)

if len(top_sort) == n:
    print(*[x + 1 for x in top_sort])
else:
    print("IMPOSSIBLE")
