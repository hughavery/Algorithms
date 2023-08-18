def transpose(adj_list):
    """swap everything"""
    num_vert = len(adj_list)
    new_graph = [[]  for _ in range(num_vert)]
    for edges in range(len(adj_list)):
        for single in adj_list[edges]:
            new_graph[single[0]].append((edges,single[1]))
    return new_graph


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