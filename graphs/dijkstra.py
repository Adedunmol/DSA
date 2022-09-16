

from collections import defaultdict, deque


graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]

        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


#print(parents)


arr = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
arr2 = [[1, 2], [2, 3], [1, 3], [4, 5], [4, 6], [5, 7], [6, 7]] 

def mod_dijsktra(arr, source, dest):
    
    if len(arr) < 1:
        return False
    
    graph = {}
    queue = []

    for edge1, edge2 in arr:
        graph[edge1] = [edge2] if graph.get(edge1) is None else graph[edge1] + [edge2]
        graph[edge2] = [edge1] if graph.get(edge2) is None else graph[edge2] + [edge1] 
 

    queue += graph.get(source)
    searched = []

    while queue:
        neighbor = queue.pop(0)

        if neighbor not in searched:
            if neighbor == dest:
                return True
            else:
                searched.append(neighbor)
                queue += graph[neighbor]

    return False

print(mod_dijsktra(arr2, 3, 6))