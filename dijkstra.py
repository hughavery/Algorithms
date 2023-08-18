def path_length(parent, start, end):
    """not dj but return shourtest vert reached so a bfs)"""
    
    i = start
    j= end
    
    dikstr = dijkstra(adj_list, start)
            
    print(dikstr)
        
        
from math import inf

#dijkstras will return a pair of parent and distance arrays
def next_vertex(in_tree, distance):
    maxx = inf
    ace = in_tree.index(False)
    for i in range(len(in_tree)):
        if in_tree[i] == False:
            if distance[i] < maxx:
                maxx = distance[i]
                ace = i
    
    return ace



def dijkstra(adj_list, start):
    num_vert = len(adj_list)
    in_tree = [False for i in range(num_vert)]
    distance = [float('inf')for i in range(num_vert)]
    parent = [None for i in range(num_vert)]
    distance[start] = 0
    while not all(in_tree) :
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if in_tree[v] == False and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return distance


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
            
    return aj_listprint(contains(poly1, poly2))