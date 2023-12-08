'''
Author: Arnav Jain
Program Name: EECS 210 Assignment 8
Function: Graph circuit finder and game tree
Inputs: None
Outputs: Whether or not the graphs are Euler circuits, whether or not the graphs satisfy Dirac's condition, whether or not the graphs satisfy Ore's condition, the winner of the game
Collaborators: Aniketh
Other sources: Stack Overflow
Creation Date: 12/0git a7/2023
'''
from game import *
# Edge class
class Edge:

    def __init__(self, x , y):
        # x and y are vertices
        self.x = x
        self.y = y

    def __eq__(self, val):
        # if val is an edge, check if the vertices are the same
        if isinstance(val, Edge):
            return {self.x, self.y} == {val.x, val.y}
        # If it isn't an edge, compare the vertices to the value
        return {self.x, self.y} == val

    def contains(self, val):
        # Check if the edge contains the input value
        return val == self.x or val == self.y

    def __hash__(self):
        # Hash the vertices
        return hash(self.x) + hash(self.y)

    def __str__(self):
        # Return the vertices as a string
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        # Return the vertices as a string 
        return self.__str__()

    def opposite_vert(self, vertex):
        # Return the opposite vertex
        if self.x == vertex:
            return self.y
        return self.x


# Graph class
class Graph:
    def __init__(self, verts, edges):
        # verts is a set of vertices
        self.verts = verts
        # edges is a set of edge classes
        self.edges = set()
        for edge in edges:
            self.edges.add(Edge(edge[0], edge[1]))
        # verts_count is the number of vertices in the graph
        self.verts_count = len(self.verts)
    
    def degree(self, vertex):
        # Count the number of edges that contain the vertex
        count = 0
        for edge in self.edges:
            # If the edge contains the vertex, increment the count, then return it
            if edge.contains(vertex):
                count += 1
        return count
    
    def odd_verts(self):
        # Return a set of vertices with odd degree

        # Initialize a set to store the odd vertices
        odd = set()
        for vert in self.verts:
            # If the degree of the vertex is odd, add it to the set
            if self.degree(vert) % 2 == 1:
                odd.add(vert)
        # Return the set
        return odd
    
    def hamilton_dirac(self):
        # Check if the graph satisfies Dirac's condition

        for vert in self.verts:
            # If the degree of the vertex is less than half the number of vertices, it is not a Hamilton circuit
            if self.degree(vert) < self.verts_count / 2:
                return False
        
        # If the loop completes, the graph satisfies Dirac's condition
        return True

    def hamilton_Ore(self):
        # Check if the graph satisfies Ore's condition

        # Convert the set of vertices to a list so we can index it
        verts_list = list(self.verts)
        for i in range(self.verts_count):
            for j in range(i + 1, self.verts_count):
                # Go through every pair of vertices and get the vertices
                vertex1 = verts_list[i]
                vertex2 = verts_list[j]

                # If they are the same edge, skip it
                if Edge(vertex1, vertex2) in self.edges:
                    continue

                # Get the sum of the degrees of the vertices
                check = self.degree(vertex1) + self.degree(vertex2)

                # If the sum is less than the number of vertices, it is not a Hamilton circuit
                if check < self.verts_count:
                    return False

        # If the loop completes, the graph satisfies Ore's condition
        return True
 
    def adj_edges(self, vertex):
        # Return a set of edges adjacent to the vertex

        # Initialize a set to store the edges
        edges = set()
        for edge in self.edges:
            # If the edge contains the vertex, add it to the set
            if edge.contains(vertex):
                edges.add(edge)
        
        # Return the set
        return edges
    
    def euler_circuit(self):
        # Return a list of vertices that form an Euler circuit

        # If there are any odd vertices, the graph does not have an Euler circuit so raise an error
        if len(self.odd_verts()) > 0:
            raise RuntimeError("Graph does not have an Euler circuit")

        # Save the current state of the graph's edges
        temp_edges = self.edges.copy()

        # Initialize a list to track vertices; start with an arbitrary vertex
        curr_vert = list(self.verts)[0]
        vertex_tracker = [curr_vert]

        # Initialize the circuit list
        euler_circuit = []

        while vertex_tracker != []: # While there are still vertices to visit
            # Select the current vertex
            curr_vert = vertex_tracker[-1]
            
            # Get the adjacent edges
            available_edges = self.adj_edges(curr_vert)

            if not available_edges:
                # If no edges are left, add the vertex to the circuit and remove it from the tracker
                euler_circuit.append(curr_vert)
                vertex_tracker.pop()
            else:
                # Remove an edge and add the opposite vertex to the tracker
                edge = available_edges.pop()
                self.edges.remove(edge)
                next_vertex = edge.opposite_vert(curr_vert)
                vertex_tracker.append(next_vertex)

        # Restore the original state of edges and return the circuit
        self.edges = temp_edges
        return euler_circuit


def main():
    print("Problem 1:")
    # Problem 1: Create the graphs and test if they are Euler circuits, if there is an error, print the odd vertices
    # Problem 1 G1
    vert = {'a', 'b', 'c', 'd', 'e'}
    edges = [('a', 'e'), ('a', 'b'), ('b', 'e'), ('e', 'd'), ('e', 'c'), ('c', 'd'), ('d', 'e')]
    p1g1 = Graph(vert, edges)
    try:
        print(f"Example 1 graph G1 is a Euler circuit: {p1g1.euler_circuit()}")
    except RuntimeError:
        print(f"Example 1 graph G1 is not a Euler circuit. The odd vertices are: {p1g1.odd_verts()}")


    # Problem 1 G2
    vert = {'a', 'b', 'c', 'd', 'e'}
    edges = [('a', 'e'), ('a', 'b'), ('b', 'e'), ('e', 'd'), ('e', 'c'), ('c', 'd'), ('d', 'e'), ('a', 'd'), ('c', 'b')]
    p1g2 = Graph(vert, edges)
    try:
        print(f"Example 1 graph G2 is a Euler circuit: {p1g2.euler_circuit()}")
    except RuntimeError:
        print(f"Example 1 graph G2 is not a Euler circuit. The odd vertices are: {p1g2.odd_verts()}")


    # Problem 1 G3
    vert = {'a', 'b', 'c', 'd', 'e'}
    edges = [('a', 'b'), ('a', 'd'), ('a', 'c'), ('b', 'd'), ('c', 'd'), ('d', 'e'), ('b', 'e')]
    p1g3 = Graph(vert, edges)
    try: 
        print(f"Example 1 graph G3 is a Euler circuit: {p1g3.euler_circuit()}")
    except RuntimeError:
        print(f"Example 1 graph G3 is not a Euler circuit. The odd vertices are: {p1g3.odd_verts()}")


    # Bridge Excersize
    vert = {'a', 'b', 'c', 'd'}
    edges = [('a', 'b'), ('b', 'a'), ('a', 'c'), ('c', 'a'), ('c', 'd'), ('d', 'a'), ('d', 'b')]
    bridge = Graph(vert, edges)
    try:
        print(f"Bridge graph is a Euler circuit: {bridge.euler_circuit()}")
    except RuntimeError:
        print(f"Bridge graph is not a Euler circuit. The odd vertices are: {bridge.odd_verts()}")


    # 1b
    vert = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
    edges = [('a', 'd'), ('a', 'b'), ('b', 'e'), ('b', 'c'), ('b', 'd'), ('c', 'f'), ('d', 'g'), ('d', 'e'), ('e', 'h'), ('e', 'f'), ('f', 'i'), ('g', 'h'), ('h', 'i'), ('h', 'f')]
    p1b = Graph(vert, edges)
    try:
        print(f"Problem 1b graph is a Euler circuit: {p1b.euler_circuit()}")
    except RuntimeError:
        print(f"Problem 1b graph is not a Euler circuit. The odd vertices are: {p1b.odd_verts()}")

    print()
    print("Problem 2:")
    # Graphs for problem 2 and 3
    # Example 5 G1
    vert = {'a', 'b', 'c', 'd', 'e'}
    edges = [('a', 'e'), ('a', 'b'), ('a', 'c'), ('b', 'e'), ('b', 'c'), ('c', 'e'), ('c', 'd'), ('e', 'd')]
    p2g1 = Graph(vert, edges)

    # Example 5 G2
    vert = {'a', 'b', 'c', 'd'}
    edges = [('a', 'b'), ('b', 'd'), ('b', 'c'), ('c', 'd')]
    p2g2 = Graph(vert, edges)

    # Example 5 G3
    vert = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    edges = [('a', 'b'), ('b', 'c'), ('b', 'g'), ('e', 'g'), ('d', 'c'), ('c', 'e'), ('e', 'f')]
    p2g3 = Graph(vert, edges)

    # Test case 2 (used for 3b also)
    vert = {'a', 'b', 'c', 'd', 'e', 'f'}
    edges = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'f'), ('d', 'e'), ('d', 'f'), ('e', 'f')]
    p2b = Graph(vert, edges)

    # Problem 2: Calls the hamilton dirac function for each graph. If it returns true, it satisfies Dirac's condition and is a Hamilton circuit, otherwise it may be a Hamilton circuit
    if p2g1.hamilton_dirac():
        print("Example 5 graph G1 satisfies Dirac's condition and is a Hamilton circuit")
    else:
        print("Example 5 graph G1 does not satisfy Dirac's condition and may be a Hamilton circuit")
    
    if p2g2.hamilton_dirac():
        print("Example 5 graph G2 satisfies Dirac's condition and is a Hamilton circuit")
    else:
        print("Example 5 graph G2 does not satisfy Dirac's condition and may be a Hamilton circuit")
    
    if p2g3.hamilton_dirac():
        print("Example 5 graph G3 satisfies Dirac's condition and is a Hamilton circuit")
    else:
        print("Example 5 graph G3 does not satisfy Dirac's condition and may be a Hamilton circuit")

    if p2b.hamilton_dirac():
        print("Test case 2 graph satisfies Dirac's condition and is a Hamilton circuit")
    else:
        print("Test case 2 graph does not satisfy Dirac's condition and may be a Hamilton circuit")    



    print()
    print("Problem 3:")
# Problem 3: Calls the hamilton ore function for each graph. If it returns true, it satisfies Dirac's condition and is a Hamilton circuit, otherwise it may be a Hamilton circuit
    if p2g1.hamilton_Ore():
        print("Example 5 graph G1 satisfies Ore's condition and is a Hamilton circuit")
    else:
        print("Example 5 graph G1 does not satisfy Ore's condition and may be a Hamilton circuit")
    
    if p2g2.hamilton_Ore():
        print("Example 5 graph G2 satisfies Ore's condition and is a Hamilton circuit")
    else:
        print("Example 5 graph G2 does not satisfy Ore's condition and may be a Hamilton circuit")
    
    if p2g3.hamilton_Ore():
        print("Example 5 graph G3 satisfies Ore's condition and is a Hamilton circuit")
    else:
        print("Example 5 graph G3 does not satisfy Ore's condition and may be a Hamilton circuit")

    if p2b.hamilton_Ore():
        print("Test case 2 graph satisfies Ore's condition and is a Hamilton circuit")
    else:
        print("Test case 2 graph does not satisfy Ore's condition and may be a Hamilton circuit")


    print()
    print("Problem 4:") 
    # Problem 4: Calls the play_game function for each game and prints the winner
    # Question 4a, print the game tree for values 2,2,1
    print("Question 4a:")
    nimSolver = NimGame(2,2,1)
    nimSolver.print_tree()

    # Question 4b, print the game tree for values 1,2,3
    print("Question 4b:")
    nimSolver = NimGame(1,2,3)
    nimSolver.print_tree()

    # Question 4c, Simulate the game 100 times and print the results
    print("Question 4c:")
    nimSolver = NimGame(2,2,1)
    nimSolver.sim()

main()