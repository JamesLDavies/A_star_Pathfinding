# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:34:13 2020

@author: James
"""


class Node():
    """Node for the a star pathfinding algorithm"""
    
    #Default values for parent and position are none, as these nodes start off as parents
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position
        
        #f = g + h
        self.f = 0 #total cost of the node
        self.g = 0 #distance between starting and current node
        self.h = 0 #estimated distance from current to end node
        

    def __eq__(self,other):
        return self.position == other.position



#Function definitions

def print_maze(grid):
    """Function to print the maze"""
    for i in range(0,len(grid)):
        print('\n',end=' ')
        for j in range(0, len(grid)):
            print(grid[i][j],end=' ')
    print('\n')
    
def astar_children(maze, current_node, open_list, closed_list, end_node):
    """astar pathfinding algo children function"""
    children = []
        
    #Positions
    up = (0,1)
    down = (0,-1)
    left = (-1,0)
    right = (1,0)
    up_right = (1,1)
    up_left = (1,-1)
    down_right = (1,-1)
    down_left = (-1,-1)
    positions = [up,down,left,right,up_right,up_left,down_right,down_left]
    
    for new_pos in positions:
        
        #Node position
        node_pos_x = current_node.position[0] + new_pos[0]
        node_pos_y = current_node.position[1] + new_pos[1]
        node_pos = (node_pos_x, node_pos_y)
        
        # Make sure within range
        if node_pos[0] > (len(maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(maze[len(maze)-1]) -1) or node_pos[1] < 0:
            continue
        
        #Check no wall is present
        if maze[node_pos[0]][node_pos[1]] != 0:
            continue
        
        #Create new node
        new_node = Node(current_node, node_pos)
        
        #Append to children list
        children.append(new_node)
        
    #Children loop
    for child in children:
        
        #Check child is on the closeed list
        for closed_child in closed_list:
            if child == closed_child:
                continue
            
        #Set f,g,h
        child.g = current_node.g + 1
        child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
        child.f = child.g + child.h
        
        #Check child is already in the open list
        for open_node in open_list:
            if child == open_node and child.g > open_node.g:
                continue
            
        #Append child to open list
        open_list.append(child)
    
    
    
def astar(maze,start_pos,end_pos):
    """astar pathfinding algorithm"""
    #Loop until end position is reached
    
    
    #start and end node initialisation
    start_node = Node(None, start_pos)
    end_node = Node(None, end_pos)
        
    #initialise open and closed lists
    open_list = []
    closed_list = []
    
    #append start_node
    open_list.append(start_node)
    
    #Loop until end_pos is found
    while len(open_list) > 0:
        
        #Obtain the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f: #item cost < current node cost
                current_node = item
                current_index = index
                
        #Move the current node to the closed list
        open_list.pop(current_index) #Remove off open list
        closed_list.append(current_node) #Append to closed list
        
        
        #Test if the end node has been found
        if current_node == end_node:
            path = []
            current = current_node 
            while current is not None: 
                path.append(current.position)
                current = current.parent
            return path[::-1] #return the path in reverse

        
        #Children nodes
        astar_children(maze, current_node, open_list, closed_list, end_node)
        
    
    



#Main
#Grid, 0 represents an empty space, 1 represents a wall
grid = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,0,0,0],
        [0,0,1,0,0,0,1,0,0,0],
        [0,0,1,0,0,0,1,0,0,0],
        [0,0,1,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0],
]

start_pos = (0,0)
end_pos = (9,9)

print('Starting maze:')
print_maze(grid)


print('Starting position is',start_pos)
print('End position is',end_pos)
print('\n')


shortest_path = astar(grid,start_pos,end_pos)
print('Shortest path is:',shortest_path)
print('Length of shortest path is: ',len(shortest_path))
print('\n')

#Print original maze with path shown
for i in range(0,len(shortest_path)):
    grid[shortest_path[i][0]][shortest_path[i][1]] = '*'

print('Maze with shortest path:')
print_maze(grid)