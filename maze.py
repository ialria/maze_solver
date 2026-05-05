import sys

class Node():
    def __init__(self, state, parent, action):
        self.state=state
        self.parent=parent
        self.action =action

class StackFrontier():
    def __init__(self):
        self.frontier=[]
    
    def add(self, node):
        self.frontier.append(node)

    def empty(self):
        return len(self.frontier)==0
    
    def contains_state(self, state):
        return any(node.state==state for node in self.frontier)
    
    def remove(self):
        if self.empty():
            raise Exception("Frontier is empty")
        else:
            node=self.frontier[-1]
            self.frontier=self.frontier[:-1]
            return node
        
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Frontier is empty")
        else:
            node=self.frontier[0]
            self.frontier=self.frontier[1:]
            return node
        
class Maze():
    def __init__(self, filename):
        with open(filename)as f:
            content=f.read()

        if content.count("A")!=1:
            raise Exception("Maze must contain exactly one start point")
        if content.count("B")!=1:
            raise Exception("Maze must contain exactly one goal")
        content=content.splitlines()
        self.height=len(content)
        self.width=max(len(line) for line in content)

        self.walls=[]
        for i in range(self.height):
            row=[]
            for j in range(self.width):
                try:
                    if content[i][j]=="A":
                        self.start=(i,j)
                        row.append(False)
                    elif content [i][j]=="B":
                        self.goal=(i,j)
                        row.append(False)
                    elif content[i][j]==" ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        self.solution=None
    
    def print(self):
        solution=self.solution[1] if self.solution is not None else None
        print()
        for i,row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█",end="")
                elif (i,j)==self.start:
                    print("A",end="")
                elif (i,j)==self.goal:
                    print("B",end="")
                elif solution is not None and (i,j) in solution:
                    print("*", end="")
                else:
                    print(" ",end="")
                
            print()
        print()

    def neighbours(self, state):
        row, col=state
        candidates=[
            ("up", (row-1, col)),
            ("down", (row+1, col)),
            ("left", (row, col-1)),
            ("right", (row, col+1))
        ]

        possible_states=[]
        for action,(r,c) in candidates:
            if 0 <=r <self.height and 0 <= c <self.width and not self.walls[r][c]:
                possible_states.append((action,(r,c)))
        return possible_states

    def solve(self):
        self.num_explored=0
        self.explored=set()

        start=Node(state=self.start, parent=None , action=None)
        frontier=StackFrontier()
        frontier.add(start)
        while True:
            if frontier.empty():
                raise Exception("No solution")
            node=frontier.remove()
            self.num_explored +=1
            self.explored.add(node.state)

            for action,state in self.neighbours(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child=Node(state=state, parent=node, action=action)
                    frontier.add(child)

            if node.state==self.goal:
                actions=[]
                cells=[]
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node=node.parent
                actions.reverse()
                cells.reverse()
                self.solution=(actions, cells)
                return
    def output_image(self, filename, show_solution =True, show_explored=False):
        from PIL import Image, ImageDraw
        cell_size=50
        cell_border=2
        img=Image.new("RGBA", (self.width*cell_size, self.height*cell_size), "black")
        draw=ImageDraw.Draw(img)
        solution=self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j,col in enumerate(row):
                if (i,j)==self.start:
                    fill=(23,40,40)
                elif (i,j)==self.goal:
                    fill=(0,0,255)
                elif solution is not None and (i,j) in solution and show_solution:
                    fill=(253,224,74)
                elif solution is not None and (i,j) in self.explored and show_explored:
                    fill=(0,84,23)

                else:
                    fill=(45,0,36)
                draw.rectangle(([(j*cell_size+cell_border, i*cell_size+cell_border),((j+1)*cell_size-cell_border, (i+1)*cell_size-cell_border)]),fill=fill)
        img.save(filename) 

        

if len(sys.argv)!=2:
    raise Exception("Usage: maze.py maze1.txt")

m=Maze(sys.argv[1])
print("Maze: ")
print()
m.print()
print("Solving:")
m.solve()
print("States explored: ", m.num_explored)
print("Solution: ")
m.print()
m.output_image("maze.png",show_explored=True)