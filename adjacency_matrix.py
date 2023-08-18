def adjacency_matrix(graph_str):
    """returns matrix as list of lists"""
    lines = graph_str.splitlines()
    header = lines[0].split(" ")
    directed = header[0] == "D"
    num_vert = int(header[1])
    weighted = len(header) > 2
    
    matrix = [[0] * num_vert for _ in range(num_vert)]
    if not weighted:
        for edge in lines[1:]:
            lis = edge.split(" ")
            end = int(lis[1])
            start = int(lis[0])
            if not directed:
                matrix[end][start] = int(1)
            matrix[start][end] = int(1)
        return matrix
    else:
        matrix = [[None] * num_vert for _ in range(num_vert)]
        for edge in lines[1:]:
            lis = edge.split(" ")
            end = int(lis[1])
            start = int(lis[0])
            weight = int(lis[2])
            if not directed:
                matrix[end][start] = weight
            matrix[start][end] = weight
        return matrix