import random

# Piles class
class Piles:
    def __init__(self, pile1, pile2, pile3):
        # Create 3 piles with the given values and store them in a tuple
        self.pile1 = pile1
        self.pile2 = pile2
        self.pile3 = pile3
        self.piles = [self.pile1, self.pile2, self.pile3]

    def __str__(self):
        # Return a string representation of the piles in the format:
        return f"{self.pile1}, {self.pile2}, {self.pile3}"

    def new_piles(self, index, value):
        # Creates a new Piles object with different values

        # Create a copy of the current piles
        temp = list(self.piles)
        # Subtract the value from the pile at the given index
        temp[index] -= value

        if sum(temp) > 0:
            # If the sum of the new piles is 0, return None
            return Piles(temp[0], temp[1], temp[2])
        
        # Return the new piles object
        return None


class GameNode:
    # GameNode class
    def __init__(self, piles, max_player=True):
        # Create a new GameNode object with the given piles, max+player is True by default because the first player is always the max player
        self.piles = piles
        self.max_player = max_player
        # Create an empty list of children and set the leaf value to 0
        self.children = []
        self.score = 0

    def add_child(self, piles):
        # Add a new child to the list of children with the same piles but with the max player switched
        self.children.append(GameNode(piles, not self.max_player))

    def get_value(self):
        # Return the value of the node

        # Internal recursive function
        def calculate_value(node):
            # If the node is a leaf node, return the leaf value
            if node.score != 0:
                return node.score
            
            # If the node is not a leaf node, return the max or min value of the children
            # depending on if the node is a max or min player
            if node.max_player:
                return max(calculate_value(child) for child in node.children)
            return min(calculate_value(child) for child in node.children)

        # Call the internal recursive function on self
        ans = calculate_value(self)

        return ans

    def __str__(self, level=0):
        # Return a string representation of the node and its children in the format:

        # Piles: <piles>, Player: <min or max>, Value: <-1 or 0 or 1>
        # The indent is based on the level of the node which is 0 by default
        indent = "\t" * level
        node_info = f"{indent}Piles: {self.piles}, "
        
        # If the node is a max player, set the player to Max, otherwise set it to Min
        player = "Max" if self.max_player else "Min"

        node_info += f"Player: {player}, "
        node_info += f"Value: {self.get_value()}\n"
        
        # Recursively call the function on the children of the node adding the info to the string and level + 1
        for child in self.children:
            node_info += child.__str__(level + 1)
        
        # Return the string
        return node_info

# NimGame class
class NimGame:
    def __init__(self, pile1, pile2, pile3):
        # Create a new NimGame object with the given piles with the Root set to a GameNode with the given piles
        self.piles = Piles(pile1, pile2, pile3)
        self.root = GameNode(self.piles)
        # Build the subtree
        self.build_subtree(self.root)

    def build_subtree(self, node):
        # Build the subtree of the given node

        # There are 3 possible moves for each pile so loop through each pile and each possible move
        for i in range(3):
            for j in range(1, node.piles.piles[i] + 1):
                # Create a new pile with the given move and add it as a child to the node (if it is a valid move)
                new_pile = node.piles.new_piles(i, j)
                if new_pile:
                    node.add_child(new_pile)
                    self.build_subtree(node.children[-1])
        # If the node is a leaf node, set the leaf value to -1 if it is a max player, otherwise set it to 1
        if not node.children:
            node.score = -1 if node.max_player else 1

    def print_tree(self):
        # Print the tree starting from the root
        print(self.root)

    def play_game(self):
        # Play the game starting from the root

        # Set the current move to the root and randomly choose who goes first
        current_move = self.root
        turn = bool(random.getrandbits(1))
        
        # While the current move has children, set the current move to the max or random child depending on who's turn it is
        print("Start:", current_move.piles)
        while current_move.children:
            if turn:
                # The max of the values of the children
                current_move = max(current_move.children, key=lambda x: x.get_value())
            else:
                current_move = random.choice(current_move.children)
            
            # Print the next move and switch who's turn it is
            player = "A" if turn else "B"
            print(f"Player {player}'s turn: ", current_move.piles)
            turn = not turn
        
        # If the current move is a max player, player A wins, otherwise player B wins
        winner = "A" if turn else "B"
        # Print the winner and return the winner
        print(winner, "is the winner")
        print()
        return winner

    def sim(self):
        # Simulate the game 100 times and print the results
        a_wins = 0
        b_wins = 0
        for _ in range(100):
            # Play the game 100 times and keep track of the number of wins for each player
            if self.play_game() == "A":
                a_wins += 1
            else:
                b_wins += 1

        # Print the results
        print(f"Player A won {a_wins} times, Player B won {b_wins} times.")


