'''
Author: Arnav Jain
Program Name: EECS 210 Assignment 4
Function: Determines if a relation is reflexive, symmetric, transitive, an equivalence relation, or a poset
Inputs: None
Outputs: Prints relations 1-10 as well as the result of the is_reflexive, reflexive_closure, is_symmetric, symmetric_closure, 
         is_transitive, transitive_closure, is_eqiv, is_antisymmetric, and is_poset functions depending on the question
Collaborators: None, all me
Other sources: Stack Overflow
Creation Date: 10/10/2023
'''

def q1_reflexive():
    '''
    Inputs: None
    Output: Prints relations 1 and 2 as well as the result of the is_reflexive function and the reflexive closure function
    Function: Determines if the relations are reflexive and finds the reflexive closure of the relations
    '''
    
    #Relation 1 and 2 as well as the sets they are defined on
    relation1 = {(1,1), (2,2), (3,3), (4,4)}
    SET1 = {1,2,3,4}
    relation2 = {('a','a'), ('c','c')}
    SET2 = {'a', 'b', 'c', 'd'}

    #Prints the relations and the results of the functions
    print("Relation 1: \t\t\t\t", relation1)
    print("Relation 1 is reflexive: \t\t", is_reflexive(relation1, SET1))
    print("Reflexive closure of relation 1: \t", reflexive_closure(relation1, SET1))
    print("Relation 2: \t\t\t\t", relation2)
    print("Relation 2 is reflexive: \t\t", is_reflexive(relation2, SET2))
    print("Reflexive closure of relation 2: \t", reflexive_closure(relation2, SET2))

def q2_symmetric():
    '''
    Inputs: None
    Output: Prints relations 3 and 4 as well as the result of the is_symmetric function and the symmetric closure function
    Function: Determines if the relations are symmetric and finds the symmetric closure of the relations
    '''

    #Relation 3 and 4 as well as the sets they are defined on
    relation3 = {(1,2), (4,4), (2,1), (3,3)}
    SET3 = {1,2,3,4}
    relation4 = {(1,2), (3,3)}
    SET4 = {1,2,3,4}

    #Prints the relations and the results of the functions-
    print("Relation 3: \t\t\t\t", relation3)
    print("Relation 3 is symmetric: \t\t", is_symmetric(relation3))
    print("Symmetric closure of relation 3: \t", symmetric_closure(relation3))
    print("Relation 4: \t\t\t\t", relation4)
    print("Relation 4 is symmetric: \t\t", is_symmetric(relation4))
    print("Symmetric closure of relation 4: \t", symmetric_closure(relation4))

def q3_transitive():
    '''
    Inputs: None
    Outputs: Prints relations 5 and 6 as well as the result of the is_transitive function and the transitive closure function
    Function: Determines if the relations are transitive and finds the transitive closure of the relations    
    '''
    #Relation 5 and 6 as well as the sets they are defined on
    relation5 = {('a', 'b'), ('d', 'd'), ('b', 'c'), ('a', 'c')}
    SET5 = {'a', 'b', 'c', 'd'}

    relation6 = {(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)}
    SET6 = {1, 2, 3}

    #Prints the relations and the results of the functions
    print("Relation 5: \t\t\t\t", relation5)
    print("Relation 5 is transitive: \t\t", is_transitive(relation5))
    print("Transitive closure of relation 5: \t", transitive_closure(relation5, SET5))
    print("Relation 6: \t\t\t\t", relation6)
    print("Relation 6 is transitive: \t\t", is_transitive(relation6))
    print("Transitive closure of relation 6: \t", transitive_closure(relation6, SET6))

def q4_equiv():
    '''
    Inputs: None
    Outputs: Prints relations 7 and 8 as well as the result of the is_eqiv function (and the reasons why)
    Function: Determines if the relations are equivalence relations
    '''

    #Relation 7 and 8 as well as the sets they are defined on
    relation7 = {(1,1),(2,2),(2,3)}
    SET7 = {1,2,3}
    relation8 = {('a','a'),('b','b'),('c','c'),('b','c'),('c','b')}
    SET8 = {'a','b','c'}

    #Prints the relations and the results of the functions
    print("Relation 7: \t\t\t\t", relation7)
    print("Relation 7 is an equivalence relation:  ", is_eqiv(relation7, SET7)[0])
    print("Reasons: \t\t\t\t", is_eqiv(relation7, SET7)[1])
    print("Relation 8: \t\t\t\t", relation8)
    print("Relation 8 is an equivalence relation:  ", is_eqiv(relation8, SET8)[0])
    print("Reasons: \t\t\t\t", is_eqiv(relation8, SET8)[1])

def q5_poset():
    '''
    Inputs: None
    Outputs: Prints relations 9 and 10 as well as the result of the is_poset function (and the reasons why)
    Function: Determines if the relations are posets
    '''
    #Relation 9 and 10 as well as the sets they are defined on
    relation9 = {(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)}
    SET9 = {1,2,3,4}
    relation10 = {(0, 0), (0, 1), (0, 2), (0, 3), (1,0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)} 
    SET10 = {0, 1, 2, 3}

    #Prints the relations and the results of the functions
    print("Relation 9: \t\t\t\t", relation9)
    print("Relation 9 is a poset: \t\t\t", is_poset(relation9, SET9)[0])
    print("Reasons: \t\t\t\t", is_poset(relation9, SET9)[1])
    print("Relation 10: \t\t\t\t", relation10)
    print("Relation 10 is a poset: \t\t", is_poset(relation10, SET10)[0])
    print("Reasons: \t\t\t\t", is_poset(relation10, SET10)[1])
def is_reflexive(relation, SET):
    '''
    Inputs: relation, a set of tuples, and SET, a set of elements
    Output: True or False
    Function: Determines if the relation is reflexive
    '''
    
    #Goes through each element in the set    
    for x in SET:
        #If the tuple (x,x) is not in the relation, the relation is not reflexive so it returns False
        if (x,x) not in relation:
            return False
    #If the function hasn't returned False by now, the relation is reflexive so it returns True
    return True

def reflexive_closure(relation, SET):
    '''
    Inputs: relation, a set of tuples, and SET, a set of elements
    Output: relation, a set of tuples
    Function: Find the reflexive closure of the relation
    '''
    #Goes through each element in the set
    for x in SET:
        #If the tuple (x,x) is not in the relation, add it to the relation
        if (x,x) not in relation:
            relation.add((x,x))
    #Returns the relation
    return relation

def is_symmetric(relation):
    '''
    Inputs: relation, a set of tuples
    Output: True or False
    Function: Determines if the relation is symmetric
    '''
    
    #Goes through each element in the relation
    for x in relation:
        #If the tuple (second element, first element) is not in the relation, the relation is not symmetric so it returns False
        if (x[1], x[0]) not in relation:
            return False
    #If the function hasn't returned False by now, the relation is symmetric so it returns True
    return True

def symmetric_closure(relation):
    '''
    Inputs: relation, a set of tuples
    Output: relation, a set of tuples
    Function: Find the symmetric closure of the relation
    '''

    #Creates a copy of the relation so the original relation is not changed (Stack Overflowed this because I didn't know how to shallow copy a set)
    return_relation = relation.copy()
    #Goes through each element in the relation
    for x in relation:
        #If the tuple (second element, first element) is not in the relation, add it to the relation copy
        if (x[1], x[0]) not in relation:
            return_relation.add((x[1], x[0]))
    #Returns the relation copy
    return return_relation

def is_transitive(relation):
    '''
    Inputs: relation, a set of tuples
    Output: True or False
    Function: Determines if the relation is transitive
    '''
    #Goes through each element in the relation
    for x in relation:
        #Goes through each element in the relation again
        for y in relation:
            #If the second element of the first tuple is the same as the first element of the second tuple, and the tuple (first element of the first tuple, second element of the second tuple) is not in the relation, the relation is not transitive so it returns False
            if x[1] == y[0] and (x[0], y[1]) not in relation:
                    return False
    #If the function hasn't returned False by now, the relation is transitive so it returns True
    return True

def transitive_closure(relation, SET):
    '''
    Inputs: relation, a set of tuples, and SET, a set of elements
    Output: relation, a set of tuples
    Function: Find the transitive closure of the relation
    '''
    set_as_a_list = list(SET)
    set_as_a_list = sorted(set_as_a_list) # First converts the set to a list, then sorts it so it can be indexed later

    matrix = [[0 for _ in range(len(SET))] for _ in range(len(SET))] # Creates a matrix of 0s with the size of the set


    for x in relation:
        matrix[set_as_a_list.index(x[0])][set_as_a_list.index(x[1])] = 1 # Adds the relations to the matrix as 1s. The index of the element in the set is the index of the element in the matrix
    
    for index in range(len(SET)):
        #Goes through the amount of elements in the set
        columns = [i for i in range(len(SET))if matrix[i][index] == 1 ] # In column index, finds all the rows that have a 1
        rows = [i for i in range(len(SET)) if matrix[index][i] == 1] # In row index, finds all the columns that have a 1
        # Essentially, in row x col x, finds where there is a 1, and adds it to a list
        

        crossprod = []
        for elem in columns:
            for elem2 in rows:
                crossprod.append((elem, elem2))
                # Creates a list of all the cross products of the rows and columns
        
        for elem in crossprod:
            if matrix[elem[0]][elem[1]] == 0:
                # If the cross product is not in the matrix, add it to the matrix and the relation
                relation.add((set_as_a_list[elem[0]], set_as_a_list[elem[1]]))
                matrix[elem[0]][elem[1]] = 1
    

    return relation # Returns the relation

def is_eqiv(relation, SET):
    '''
    Inputs: relation, a set of tuples, and SET, a set of elements
    Output: True or False, and a list of reasons why
    Function: Determines if the relation is an equivalence relation and why
    '''
    reasons = []

    #Calls the reflexive, symmetric, and transitive functions to determine if the relation is an equivalence relation
    #If any of them return false (add the respective reason to the list), the relation is not an equivalence relation
    if not is_reflexive(relation, SET):
        reasons.append("Not reflexive")
    if not is_symmetric(relation):
        reasons.append("Not symmetric")
    if not is_transitive(relation):
        reasons.append("Not transitive")

    #If the length of reasons is 0, the relation is an equivalence relation, return True and the reasons why
    if len(reasons) == 0:
        reasons.append("Reflexive, symmetric, and transitive")
        return True, reasons
    #If the length of reasons is not 0, the relation is not an equivalence relation, return False and the reasons why
    return (False, reasons)

def is_antisymmetric(relation):
    '''
    Inputs: relation, a set of tuples
    Output: True or False
    Function: Determines if the relation is antisymmetric
    '''
    # Iterate over each pair in the relation
    for x in relation:
        # Check if the reverse of the current pair is in the relation
        if (x[1], x[0]) in relation:
            # If both (a, b) and (b, a) are in the relation, and a != b, then the relation is not antisymmetric (Because antisymmetric allows both pairs only if a = b)
            if x[0] != x[1]:
                return False
    # If the function hasn't returned False by now, the relation is antisymmetric
    return True
 
def is_poset(relation, SET):
    #Calls the reflexive, antisymmetric, and transitive functions to determine if the relation is a poset
    reasons = []

    #If any of them return false (add the respective reason to the list), the relation is not a poset
    if not is_reflexive(relation, SET):
        reasons.append("Not reflexive")
    if not is_antisymmetric(relation):
        reasons.append("Not antisymmetric")
    if not is_transitive(relation):
        reasons.append("Not transitive")
    
    #If the length of reasons is 0, the relation is a poset, return True and the reasons why
    if len(reasons) == 0:
        reasons.append("Reflexive, antisymmetric, and transitive")
        return True, reasons
    #If the length of reasons is not 0, the relation is not a poset, return False and the reasons why
    return (False, reasons)


def main():
    '''
    Inputs: None
    Outputs: None
    Function: Calls all the functions
    '''
    
    #Calls all the functions with \n between each one
    q1_reflexive()
    print("\n")
    q2_symmetric()
    print("\n")
    q3_transitive()
    print("\n")
    q4_equiv()
    print("\n")
    q5_poset()

if __name__ == "__main__":
    main()