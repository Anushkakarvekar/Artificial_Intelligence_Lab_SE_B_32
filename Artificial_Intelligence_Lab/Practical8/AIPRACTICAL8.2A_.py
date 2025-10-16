import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g  # cost from start to node
        self.h = h  # heuristic (estimated cost to goal)
        self.f = g + h  # total cost

    def __lt__(self, other):  # for priority queue
        return self.f < other.f

def astar_search(graph, heuristics, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristics[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.name == goal:
            path = []
            while current:
                path.append(current.name)
                current = current.parent
            return path[::-1]  # reverse path

        closed_set.add(current.name)

        for neighbor, cost in graph[current.name].items():
            if neighbor in closed_set:
                continue

            g = current.g + cost
            h = heuristics.get(neighbor, 0) 
            neighbor_node = Node(neighbor, current, g, h)

            # check if a better path exists
            if any(open_node.name == neighbor and open_node.f <= neighbor_node.f for open_node in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None

# Example Graph (with distances)
graph = {

'Home':{'Bank':45,'Garden':40,'School':50},
'Bank':{'Police Station':60,'Home':45},
'Police Station':{'Bank':60,'University':28},
'University':{'Police Station':28,'Railway Station':40},
'Railway Station':{'School':75,'Garden':72,'University':40},
'School':{'Home':50,'Post office':59,'Railway Station':40},
'Garden':{'Home':40,'Railway Station':72},
'Post office': {}
}

# Heuristic values (straight-line estimates to goal 'G')
heuristics = {
   'Home':120,
   'Bank':80,
   'Police Station':110,
   'Railway Station':20,
   'School':70,
   'Garden':100,
   'Post office':26,
}

# Run A* Search
start, goal = 'Home', 'University'
path = astar_search(graph, heuristics, start, goal)
print(f"Shortest path from {start} to {goal}: {path}")





