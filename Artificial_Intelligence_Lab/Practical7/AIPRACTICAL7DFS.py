def dfs_path(maze, start, end):
    stack = [(start, [start])]  # Stack stores tuples: (current_position, path_so_far)
    visited = set()
    
    while stack:
        position, path = stack.pop()
        x, y = position
        
        if position == end:
            return path  # Return the path when end is reached
        
        visited.add(position)
        
        # Explore neighbors: up, down, left, right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            new_pos = (new_x, new_y)
            
            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                maze[new_x][new_y] != '#' and new_pos not in visited):
                stack.append((new_pos, path + [new_pos]))
    
    return None  # Return None if no path found


# Maze definition with S=start and E=end
maze = [
    ['#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', 'E', '#'],
    ['#', '#', '#', '#', '#', '#']
]

# Start and end positions based on S and E in the maze
start = (1, 1)  # Position of 'S'
end = (4, 4)    # Position of 'E'

path = dfs_path(maze, start, end)

if path:
    print("Path found:")
    print(path)
else:
    print("No path found")

