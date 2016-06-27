from Queue import Queue

def inbound(x, y, n, m):
    return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

def bfs(grid, start_node, end_node):
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    if not (n and m):
        return []
    if start_node == end_node or not end_node.passable:
        return []
        
    back_trace = {}
    
    adj = ((+1, 0), (-1, 0), (0, +1), (0, -1))
    
    queue = Queue()
    queue.put(start_node)
    while not queue.empty() and not end_node in back_trace:
        node = queue.get()
        for adj_pair in adj:
            x = node.position.x + adj_pair[0]
            y = node.position.y + adj_pair[1]
            if not inbound(x, y, n, m) or not grid[x][y].passable:
                continue
            if grid[x][y] in back_trace:
                continue
            back_trace[grid[x][y]] = node
            queue.put(grid[x][y])
    return back_trace

def find_shortest_path(grid, start_node, end_node):
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    if not (n and m):
        return []
    back_trace = bfs(grid, start_node, end_node)
    path = []
    node = end_node
    while node != start_node:
        path.append(node)
        node = back_trace[node]
    path.append(start_node)
    path = path[: : -1]
    return path
    
