
'''
https://www.codewars.com/kata/58663693b359c4a6560001d6/train/python

Maze Runner


directions = ["N","N","N","N","N","E","E","E","E","E"])            

0 = Safe place to walk
1 = Wall
2 = Start Point
3 = Finish Point

# resolution
 find out the position of "2" in the maze p = maze[7][1]

loop the directions:
if d == "N"
    position maze[7-1][1]
   d == "S" 
    position maze[7+1][1]
   d == "E"
    position maze[7][1+1]
   d == "W"
    position maze[7-1][1-1]
    
'''

maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

def start_p(maze):
    p = maze[0][0]
    for i in range(len(maze)):
        r = 0
        for j in maze[i]:
            if maze[i][r] == 2:
                return [i,r]
            r = r + 1    

def finish_p(maze):
    p = maze[0][0]
    for i in range(len(maze)):
        r = 0
        for j in maze[i]:
            if maze[i][r] == 3:
                return [i,r]
            r = r + 1    
def maze_runner(maze, directions):
    # Code Here
    start = start_p(maze)
    finish = finish_p(maze)
    for d in directions:
        if d == "N":
            start[0] = start[0] - 1
        elif d == "S":
            start[0] = start[0] + 1
        elif d == "E":
            start[1] = start[1] + 1
        elif d == "W":
            start[1] = start[1] - 1
        print(start)
        if start == finish:
            return "Finish"
        elif start == 1:
            return "Dead"  
        elif start[0] >= len(maze) or start[1] > len(maze):
            return "Dead"
        elif start[0] <0 or start[1] <= 0:
            return "Dead"
    
    return "Lost"
        
test = maze_runner(maze, ["N","N","N","N","N","E","E","S","S","S","S","S","S"])
print(test)