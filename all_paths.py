def all_paths(adj_list, source, destination):
    solutions = []
    dfs_backtrack((source,), adj_list, solutions,destination)
    return solutions


def dfs_backtrack(candidate, input_data, output_data, destination):
    if should_prune(candidate):
        return
    if is_solution(candidate, destination):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data,destination)


def add_to_output(candidate, output_data):
    output_data.append(candidate)


def should_prune(candidate):
    return False

def is_solution(candidate_path, destination):
    """Returns True if the candidate is complete solution"""
    return candidate_path[-1] == destination

def children(candidate_path, adj_list):
    """Returns a collestion of candidates that are the children of the given
    candidate."""
    children = []
    for i, weight in adj_list[candidate_path[-1]]:
        if i not in candidate_path:
            children.append(candidate_path+(i,))
    return children

def adjacency_list(graph_str):
    
    lines = graph_str.splitlines()
    header = lines[0].split(" ")
    directed = header[0] == "D"
    num_v = int(header[1])
    weighted = len(header) > 2
    adj_list = [[]  for _ in range(num_v)]

    for edge in lines[1:]:
        edges = edge.split(" ")
        if weighted:
            weight = int(edges[2])
        else:
            weight = None
        start = int(edges[0])
        end = int(edges[1])
        if not directed:
            adj_list[end].append((start,weight))   
        adj_list[start].append((end,weight))   
    return adj_list