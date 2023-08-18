def dfs_tree(adj_list, start):
    """a"""
    vert = len(adj_list)
    state = ['U' for i in range(vert)]
    parents = [None for i in range(vert)]
    state[start] = 'D'
    return dfs_loop(adj_list,start,state,parents)

def dfs_loop(adj_list, u, state, parents):
    """yeh does a thing recursively"""
    for v in adj_list[u]:
        if state[v[0]] == 'U':
            state[v[0]] = 'D'
            parents[v[0]] = u
            dfs_loop(adj_list,v[0],state,parents)
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