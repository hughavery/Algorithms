def distance_matrix(adj_list):
    """distance from vert to vert"""
    num_v = len(adj_list)
    matrix = [[float("inf") for i in range(num_v)] for i in range(num_v)]

    for i in range(num_v):
        matrix[i][i] = 0
    
    for i in range(num_v):
        for j in adj_list[i]:
            matrix[i][j[0]] = j[1]
            
            
    return matrix



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