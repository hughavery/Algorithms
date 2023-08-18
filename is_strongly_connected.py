def transpose(adj_list):
    """swap everything"""
    num_vert = len(adj_list)
    new_graph = [[]  for _ in range(num_vert)]
    for edges in range(len(adj_list)):
        for single in adj_list[edges]:
            new_graph[single[0]].append((edges,single[1]))
    return new_graph
            

def is_strongly_connected(adj_list):
    transpose_of_list = transpose(adj_list)
    
    first = bfs_tree(adj_list,0)
    trans = bfs_tree(transpose_of_list,0)
    
    if len([[] for i in first if i == None]) > 1:
        return False
    if len([[] for i in trans if i == None]) > 1:
        return False    
    return True

def bfs_tree(adj_list,start):
    """a"""
    vert = len(adj_list)
    queue = []
    parents = [None for i in range(vert)]
    state = ['U' for i in range(vert)]
    state[start] = 'D'
    queue.append(start)
    while len(queue) != 0:
        i = queue.pop(0)
        for v in adj_list[i]:
            if state[v[0]] == 'U':
                state[v[0]] = 'D'
                parents[v[0]] = i
                queue.append(v[0])
            state[i] = 'P'
    return parents

def adjacency_list(graph_str):
    lines = graph_str.splitlines()
    header = lines[0].split(" ")
    directed = header[0] == "D"
    num_vert = int(header[1])
    weighted = len(header) > 2
    
    aj_list = [[]  for _ in range(num_vert)]
    
 
    for edge in lines[1:]:
        split = edge.split(" ")
        if weighted:
            weight = int(split[2])
        else:
            weight = None
        start = int(split[0])
        end = int(split[1])
        if not directed:
            aj_list[end].append((start,weight))    
        aj_list[start].append((end,weight))
            
    return aj_list