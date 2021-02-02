import queue
import time

# This is the goal configuration of the cube
goal = [0, 1, 2, 3, 4, 5]

# Define the Triple Class
class Triple:
    x = -1
    y = -1
    z = -1

    def __init__(self, givenX, givenY, givenZ):
        self.x = givenX
        self.y = givenY
        self.z = givenZ

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

# Define coordinate array
coordinate = [[[Triple(-1, -1, -1) for i in range(3)] for j in range(4)] for k in range(6)]

# Define the Pair class
class Pair:
    x = None
    y = None

    def __init__(self, givenX, givenY):
        self.x = givenX
        self.y = givenY

    def getX():
        return self.x

    def getY():
        return self.y

    def getSum():
        return self.x + self.y

# Define the Cube class
class Cube:
    def __init__(self, givenAction, givenCost, givenCube, givenState):
        self.action = givenAction
        self.costs = givenCost
        self.parent = givenCube
        self.state = givenState

    def __eq__(self, other):
        return self.costs.x + self.costs.y == other.costs.x + other.costs.y

    def __ne__(self, other):
        return not (self.costs.x + self.costs.y == other.costs.x + other.costs.y)

    def __lt__(self, other):
        return self.costs.x + self.costs.y < other.costs.x + other.costs.y

    def __le__(self, other):
        return self.costs.x + self.costs.y <= other.costs.x + other.costs.y

    def __gt__(self, other):
        return self.costs.x + self.costs.y > other.costs.x + other.costs.y

    def __ge__(self, other):
        return self.costs.x + self.costs.y >= other.costs.x + other.costs.y
        
    def getAction():
        return self.action

    def getParent():
        return self.parent

    def getCosts():
        return self.costs

    def getState():
        return self.state

# Initialize the coordinate to cube mapping array
def initialize_coordinates():
    # face 0
    coordinate[0][0][0] = Triple(3, 0, 2)
    coordinate[0][0][1] = Triple(3, 1, 2)
    coordinate[0][0][2] = Triple(3, 2, 2)
    coordinate[0][1][0] = Triple(4, 0, 0)
    coordinate[0][1][1] = Triple(4, 0, 1)
    coordinate[0][1][2] = Triple(4, 0, 2)
    coordinate[0][2][0] = Triple(1, 0, 0)
    coordinate[0][2][1] = Triple(1, 1, 0)
    coordinate[0][2][2] = Triple(1, 2, 0)
    coordinate[0][3][0] = Triple(5, 0, 0)
    coordinate[0][3][1] = Triple(5, 0, 1)
    coordinate[0][3][2] = Triple(5, 0, 2)
    
    # face 1
    coordinate[1][0][0] = Triple(0, 0, 2)
    coordinate[1][0][1] = Triple(0, 1, 2)
    coordinate[1][0][2] = Triple(0, 2, 2)
    coordinate[1][1][0] = Triple(4, 0, 2)
    coordinate[1][1][1] = Triple(4, 1, 2)
    coordinate[1][1][2] = Triple(4, 2, 2)
    coordinate[1][2][0] = Triple(2, 0, 0)
    coordinate[1][2][1] = Triple(2, 1, 0)
    coordinate[1][2][2] = Triple(2, 2, 0)
    coordinate[1][3][0] = Triple(5, 0, 2)
    coordinate[1][3][1] = Triple(5, 1, 2)
    coordinate[1][3][2] = Triple(5, 2, 2)
    
    # face 2
    coordinate[2][0][0] = Triple(1, 0, 2)
    coordinate[2][0][1] = Triple(1, 1, 2)
    coordinate[2][0][2] = Triple(1, 2, 2)
    coordinate[2][1][0] = Triple(4, 2, 2)
    coordinate[2][1][1] = Triple(4, 2, 1)
    coordinate[2][1][2] = Triple(4, 2, 0)
    coordinate[2][2][0] = Triple(3, 0, 0)
    coordinate[2][2][1] = Triple(3, 1, 0)
    coordinate[2][2][2] = Triple(3, 2, 0)
    coordinate[2][3][0] = Triple(5, 2, 2)
    coordinate[2][3][1] = Triple(5, 2, 1)
    coordinate[2][3][2] = Triple(5, 2, 0)
    
    # face 3
    coordinate[3][0][0] = Triple(2, 0, 2)
    coordinate[3][0][1] = Triple(2, 1, 2)
    coordinate[3][0][2] = Triple(2, 2, 2)
    coordinate[3][1][0] = Triple(4, 2, 0)
    coordinate[3][1][1] = Triple(4, 1, 0)
    coordinate[3][1][2] = Triple(4, 0, 0)
    coordinate[3][2][0] = Triple(0, 0, 0)
    coordinate[3][2][1] = Triple(0, 1, 0)
    coordinate[3][2][2] = Triple(0, 2, 0)
    coordinate[3][3][0] = Triple(5, 2, 0)
    coordinate[3][3][1] = Triple(5, 1, 0)
    coordinate[3][3][2] = Triple(5, 0, 0)
    
    # face 4
    coordinate[4][0][0] = Triple(3, 2, 2)
    coordinate[4][0][1] = Triple(3, 2, 1)
    coordinate[4][0][2] = Triple(3, 2, 0)
    coordinate[4][1][0] = Triple(2, 2, 2)
    coordinate[4][1][1] = Triple(2, 2, 1)
    coordinate[4][1][2] = Triple(2, 2, 0)
    coordinate[4][2][0] = Triple(1, 2, 0)
    coordinate[4][2][1] = Triple(1, 2, 1)
    coordinate[4][2][2] = Triple(1, 2, 2)
    coordinate[4][3][0] = Triple(0, 2, 0)
    coordinate[4][3][1] = Triple(0, 2, 1)
    coordinate[4][3][2] = Triple(0, 2, 2)
    
    # face 5
    coordinate[5][0][0] = Triple(3, 0, 2)
    coordinate[5][0][1] = Triple(3, 0, 1)
    coordinate[5][0][2] = Triple(3, 0, 0)
    coordinate[5][1][0] = Triple(2, 0, 2)
    coordinate[5][1][1] = Triple(2, 0, 1)
    coordinate[5][1][2] = Triple(2, 0, 0)
    coordinate[5][2][0] = Triple(1, 0, 0)
    coordinate[5][2][1] = Triple(1, 0, 1)
    coordinate[5][2][2] = Triple(1, 0, 2)
    coordinate[5][3][0] = Triple(0, 0, 0)
    coordinate[5][3][1] = Triple(0, 0, 1)
    coordinate[5][3][2] = Triple(0, 0, 2)

# check if the given rubiks cube state is the goal state
def isGoal(state):
    for face in range(6):
        for i in range(3):
            for j in range(3):
                if not (state[face][i][j] == state[face][0][0]):
                    return False
    return True

# Make changes to the face of the given cube that has turned left
def intraface_turn_left(face, state):
    save = state[face][0][0]
    state[face][0][0] = state[face][2][0]
    save2 = state[face][0][2]
    state[face][0][2] = save
    save3 = state[face][2][2]
    state[face][2][2] = save2
    state[face][2][0] = save3

    save = state[face][0][1]
    state[face][0][1] = state[face][1][0]
    save2 = state[face][1][2]
    state[face][1][2] = save
    save3 = state[face][2][1]
    state[face][2][1] = save2
    state[face][1][0] = save3

    return state

# Turn the face of the given cube to the left
def turn_left(face, state):
    simulated_state = [[[-1 for i in range(3)] for j in range(3)] for k in range(6)]

    for i in range(6):
        for j in range(3):
            for k in range(3):
                simulated_state[i][j][k] = state[i][j][k]

    simulated_state = intraface_turn_left(face, simulated_state)

    values = [-1 for i in range(12)]
    count = 0
    count2 = 0

    for d in range(4):
        for order in range(3):
            cord = coordinate[face][d][order]
            values[count] = simulated_state[cord.getX()][cord.getY()][cord.getZ()]
            count += 1

    for i in range(4):
        if i % 2 == 1:
            for order in range(3):
                if i == 0:
                    cord = coordinate[face][3][order]
                else:
                    cord = coordinate[face][i-1][order]
                simulated_state[cord.getX()][cord.getY()][cord.getZ()] = values[count2]
                count2 += 1
        else:
            for fake_order in range(3):
                order = 2 - fake_order
                if i == 0:
                    cord = coordinate[face][3][order]
                else:
                    cord = coordinate[face][i-1][order]
                simulated_state[cord.getX()][cord.getY()][cord.getZ()] = values[count2]
                count2 += 1

    return simulated_state

# Make changes to the face of the given cube that has turned right
def intraface_turn_right(face, state):
    save = state[face][0][0]
    state[face][0][0] = state[face][0][2]
    save2 = state[face][2][0]
    state[face][2][0] = save
    save3 = state[face][2][2]
    state[face][2][2] = save2
    state[face][0][2] = save3

    save = state[face][0][1]
    state[face][0][1] = state[face][1][2]
    save2 = state[face][1][0]
    state[face][1][0] = save
    save3 = state[face][2][1]
    state[face][2][1] = save2
    state[face][1][2] = save3

    return state

# Turn the face of the given cube to the right
def turn_right(face, state):
    simulated_state = [[[-1 for i in range(3)] for j in range(3)] for k in range(6)]

    for i in range(6):
        for j in range(3):
            for k in range(3):
                simulated_state[i][j][k] = state[i][j][k]

    simulated_state = intraface_turn_right(face, simulated_state)

    values = [-1 for i in range(12)]
    count = 0
    count2 = 0

    for d in range(4):
        for order in range(3):
            cord = coordinate[face][d][order]
            values[count] = simulated_state[cord.getX()][cord.getY()][cord.getZ()]
            count += 1

    for i in range(4):
        if i % 2 == 0:
            for order in range(3):
                cord = coordinate[face][(i+1)%4][order]
                simulated_state[cord.getX()][cord.getY()][cord.getZ()] = values[count2]
                count2 += 1
        else:
            for fake_order in range(3):
                order = 2 - fake_order
                cord = coordinate[face][(i+1) % 4][order]
                simulated_state[cord.getX()][cord.getY()][cord.getZ()] = values[count2]
                count2 += 1

    return simulated_state

# Run A star algorithm to solve the given cube
def astar(initial_cube):
    frontier = queue.PriorityQueue(maxsize=0)
    exploredSet = []

    frontier.put(initial_cube)
    while not frontier.empty():
        current_cube = frontier.get()
        for face in range(6):
            new_cube = turn_left(face, current_cube.state)
            if exploredSet.count(new_cube) > 0:
                continue
            addCube = Cube(Pair(face, 0), Pair(current_cube.costs.x + 12, heuristic(new_cube)), current_cube, new_cube)
            if isGoal(new_cube):
                return addCube
            frontier.put(addCube)
            exploredSet.append(new_cube)

        for face in range(6):
            new_cube = turn_right(face, current_cube.state)
            if exploredSet.count(new_cube) > 0:
                continue
            addCube = Cube(Pair(face, 1), Pair(current_cube.costs.x + 12, heuristic(new_cube)), current_cube, new_cube)
            if isGoal(new_cube):
                return addCube
            frontier.put(addCube)
            exploredSet.append(new_cube)

    return None

# Calculate the value we associate to the given face
def isAcross(face, goal_face):
    if face < 4 and goal_face < 4 and abs(face - goal_face) == 2:
        return True
    elif face >= 4 and goal_face >= 4 and abs(face - goal_face) == 1:
        return True
    
    return False

# Calculate the heuristic value of the state (how good that state is)
def heuristic(state):
    sum_val = 0

    for i in range(6):
        for j in range(3):
            for k in range(3):
                goal_face = goal[int(state[i][j][k]) - 1]
                if isAcross(i, goal_face):
                    sum_val += 2
                elif i != goal_face:
                    sum_val += 1
    return sum_val


# Initialize the coordinate mapping
initialize_coordinates()

# Initialize the cube you want to be solved
initial_cube = [[[-1 for i in range(3)] for j in range(3)] for k in range(6)]

# Get the cube input from user
for i in range(6):
    print("Give the cube(starting at top left) of face: ", i)
    for j in range(3):
        for k in range(3):
            initial_cube[i][j][k] = input()

# Get the result, which is a sequence of turns user must do
# to solve the cube
result = astar(Cube(Pair(-1, -1), Pair(0, heuristic(initial_cube)), None, initial_cube))

# If the resulting state is solved, print the turns necessary
# Or else print that the state isn't solvable
if isGoal(result.state):
    print("In order to solve the cube, do these actions")
    while not result.action.x == -1:
        if(result.action.y == 0):
            print("Turn Face ", result.action.x, " to the left")
        else:
            print("Turn Face ", result.action.x, " to the right")
        result = result.parent
else:
    print("Not solvable")

