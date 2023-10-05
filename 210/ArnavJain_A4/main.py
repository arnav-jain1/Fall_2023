

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


q1_reflexive()
print("\n")
q2_symmetric()