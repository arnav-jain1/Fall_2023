"""
EECS 210 Assignment 3
Python code for demonstrating operations on relations and properties of relations.

Inputs: None
Output: Print out of the name of each exercise, followed by the exercise's output.
Collaborators: None 
Other sources for the code: ChatGPT for reflexive part of q4
Full name: Arnav Jain
Creation date: 9-26-23
"""


def main():
    # Printing and calling the functions for each question
    print("Question 1: ")
    q1()
   
    print("\nQuestion 2: ")
    q2()
  
    print("\nQuestion 3: ")
    q3()

    print()
    q4()
def q1():
    """
    Function to demonstrate union, intersection, and difference operations on two sets.
    Inputs: None
    Output: Prints the union, intersection, and difference of two sets.
    """
    
    # Defining two sets
    set1 = {(1,1), (2,2), (3,3)} 
    set2 = {(1,1), (1,2), (1,3), (1,4)}

    # Printing the respective function 
    print("Union: \t\t" + str(set1.union(set2)))
    print("Intersection: \t" + str(set1.intersection(set2)))
    print("Set 1 - set 2: \t" + str(set1.difference(set2)))
    print("Set 2 - set 1: \t" + str(set2.difference(set1)))

def q2():
    """
    Function to demonstrate the composite operation on two sets.
    Inputs: None
    Outputs: Prints the composite of two sets.
    """

    # Defining two sets 
    r = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}
    s = {(1, 0), (2, 0), (3, 1), (3, 2), (4, 1)}


    #Prints the composite of s and r by calling the composite function

    print(composite(s, r))


def composite(set1, set2):
    """
    Function to calculate the composite of two sets.
    Inputs: 2 sets
    Outputs: Returns set that is the composite of the two sets
    """

    #Creates a set to store the solution
    sol = set()
    for elem in set1:
        #Goes through set 1
        for elem2 in set2:
            #Goes through set 2
            if elem[1] == elem2[0]:
                #If the second element of the first set is equal to the first element of the second set
                #Then it adds the first element of the first set and the second element of the second set to the solution
                sol.add((elem[0], elem2[1]))
    #Returns the solution
    return sol

def q3():
    """
    Function to demonstrate the square of a set.
    Inputs: None
    Outputs: Prints the square of a set.
    """
    set1 = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}
    print(composite(set1, set1))

def q4():
    """
    Function to analyze properties of a relation: reflexive, symmetric, antisymmetric, and transitive.
    Based on the relation {(x, y) | x + y = 0} on the set {-10, -9, ..., 9, 10}.
    Inputs: None
    Outputs: Prints the relation, and whether it is reflexive, symmetric, antisymmetric, and transitive.
    """
    set1 = set()
    #Creates a set to store the relation, goes through all the numbers between -10 and 10 twice and adds them to the set if they add up to 0
    for num in range(-10, 11, 1):
        for num2 in range(-10, 11, 1):
            if num + num2 == 0:
                set1.add((num, num2))
    #Prints the output
    print("Set: \n" + str(set1))

    reflexive = all(((x, x) in set1) for x in range(-10, 11, 1))
    #True if all the numbers between -10 and 10 are in set1 as (x, x)
    #Used chatGPT for this part because I didn't know that you can do the (x,x) in set1 part. Once I figured that out the rest was easy


    symmetric = all(((y, x) in set1) for (x, y) in set1) 
    #True if the reverse of all the elements in set1 are in set1


    antisymmetric = all(((y, x) not in set1) for (x, y) in set1 if x != y)
    #True if the reverse of all the elements in set1 while making sure the edge case of x==y is not counted


    #Transitive True until proven false
    transitive = True
    for a, b in set1:
        #For a and b in set 1
        for c, d in set1:
            #for b and c in set 1
            if b == c:
                #if b and c are the same
                if (a, d) not in set1:
                    #Checks to see if (a, d) is in set1 if it is not then it is not transitive
                    transitive = False
                    break
    
    #Prints the answers
    print("Reflexive: \t" + str(reflexive))
    print("Symmetric: \t" + str(symmetric))
    print("Antisymmetric \t" + str(antisymmetric))
    print("Transitive: \t" + str(transitive))
if __name__ == "__main__":
    main()
    # Calling the main function