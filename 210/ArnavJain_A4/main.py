

def q1_reflexive():
    relation1 = {(1,1), (2,2), (3,3), (4,4)}
    SET1 = {1,2,3,4}
    relation2 = {('a','a'), ('c','c')}
    SET2 = {'a', 'b', 'c', 'd'}
    print("Relation 1: \t\t\t\t", relation1)
    print("Relation 1 is reflexive: \t\t", is_reflexive(relation1, SET1))
    print("Reflexive closure of relation 1: \t", reflexive_closure(relation1, SET1))
    print("Relation 2: \t\t\t\t", relation2)
    print("Relation 2 is reflexive: \t\t", is_reflexive(relation2, SET2))
    print("Reflexive closure of relation 2: \t", reflexive_closure(relation2, SET2))

def q2_symmetric():
    relation3 = {(1,2), (4,4), (2,1), (3,3)}
    SET3 = {1,2,3,4}
    relation4 = {(1,2), (3,3)}
    SET4 = {1,2,3,4}
    print("Relation 3: \t\t\t\t", relation3)
    print("Relation 3 is symmetric: \t\t", is_symmetric(relation3))
    print("Symmetric closure of relation 3: \t", symmetric_closure(relation3))
    print("Relation 4: \t\t\t\t", relation4)
    print("Relation 4 is symmetric: \t\t", is_symmetric(relation4))
    print("Symmetric closure of relation 4: \t", symmetric_closure(relation4))

def q3_transitive():
    relation5 = {('a', 'b'), ('d', 'd'), ('b', 'c'), ('a', 'c')}
    SET5 = {'a', 'b', 'c', 'd'}

    relation6 = {(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)}
    SET6 = {1, 2, 3}

    print("Relation 5: \t\t\t\t", relation5)
    print("Relation 5 is transitive: \t\t", is_transitive(relation5))
    print("Transitive closure of relation 5: \t", transitive_closure(relation5, SET5))
    print("Relation 6: \t\t\t\t", relation6)
    print("Relation 6 is transitive: \t\t", is_transitive(relation6))
    print("Transitive closure of relation 6: \t", transitive_closure(relation6, SET6))

def q4_equiv():
    relation7 = {(1,1),(2,2),(2,3)}
    SET7 = {1,2,3}
    relation8 = {('a','a'),('b','b'),('c','c'),('b','c'),('c','b')}
    SET8 = {'a','b','c'}

    print("Relation 7: \t\t\t\t", relation7)
    print("Relation 7 is an equivalence relation:  ", is_eqiv(relation7, SET7)[0])
    print("Reasons: \t\t\t\t", is_eqiv(relation7, SET7)[1])
    print("Relation 8: \t\t\t\t", relation8)
    print("Relation 8 is an equivalence relation:  ", is_eqiv(relation8, SET8)[0])
    print("Reasons: \t\t\t\t", is_eqiv(relation8, SET8)[1])


def is_reflexive(relation, SET):
    for x in SET:
        if (x,x) not in relation:
            return False
    return True

def reflexive_closure(relation, SET):
    for x in SET:
        if (x,x) not in relation:
            relation.add((x,x))
    return relation

def is_symmetric(relation):
    for x in relation:
        if (x[1], x[0]) not in relation:
            return False
    return True

def symmetric_closure(relation):
    return_relation = relation.copy()
    for x in relation:
        if (x[1], x[0]) not in relation:
            return_relation.add((x[1], x[0]))
    return return_relation

def is_transitive(relation):
    for x in relation:
        for y in relation:
            if x[1] == y[0] and (x[0], y[1]) not in relation:
                    return False
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
    reasons = []

    if not is_reflexive(relation, SET):
        reasons.append("Not reflexive")
    if not is_symmetric(relation):
        reasons.append("Not symmetric")
    if not is_transitive(relation):
        reasons.append("Not transitive")
    if len(reasons) == 0:
        reasons.append("Reflexive, symmetric, and transitive")
        return True, reasons
    return (False, reasons)

# q1_reflexive()
# print("\n")
# q2_symmetric()
# print("\n")
# q3_transitive()
# print("\n")
q4_equiv()

