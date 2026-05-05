🧩 Maze Solver (BFS & DFS in Python)

A visual maze-solving project built in Python that demonstrates classic graph search algorithms like Breadth-First Search (BFS) and Depth-First Search (DFS).

This program reads a maze from a text file, solves it using algorithms, and generates a visual representation of the solution path.

 Features
- 🧠 Breadth-First Search (BFS) → finds the shortest path
- 🔍 Depth-First Search (DFS) → explores deep paths
- 📂 Reads maze from `.txt` files
- 🧭 Tracks explored nodes
- 🖼️ Generates visual output (`maze.png`)
- 🎯 Identifies start (A) and goal (B)
- ⭐ Highlights the final solution path

📁 Project Structure
maze_solver/
├── maze.py          # Main solver (BFS & DFS)
├── maze1.txt        # Sample maze input
├── maze2.txt        # Sample maze input
├── maze.png         # Generated solution image
└── README.md        # Project documentation

▶️ How to Run

Install required dependency:
pip install pillow

Run the program:
python maze.py maze1.txt

python maze.py maze2.txt

 How It Works
Each maze is treated as a graph:
- Each cell = a node
- Moves = edges (up, down, left, right)
- A = Start point
- B = Goal point

 Algorithms used:
- BFS (Queue-based) → guarantees shortest path
- DFS (Stack-based) → explores deep paths first

 Maze Symbols
A → Start  
B → Goal  
█ → Wall  
* → Solution path  
(space) → Open path  

 Output
The program generates a file called:

maze.png

It visually shows:
- Yellow path → solution
- Explored nodes (optional)
- Start and goal positions

 What I Learned
- Graph search algorithms (BFS & DFS)
- Object-Oriented Programming in Python
- File handling and parsing
- Pathfinding logic
- Image generation using Pillow
- Real-world problem solving
