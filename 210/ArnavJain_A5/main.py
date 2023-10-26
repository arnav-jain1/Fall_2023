
def is_func(A, B, f):
    '''
    Inputs: A, B, f (A and B are sets, f is a list of tuples)
    Note: A and B are unused in this function
    Output: True if f is a function, False otherwise
    Function: Tests if f is a function
    '''

    #First make an empty dictionary
    vals = dict()

    #Loop through each element in f
    for elem in f:
        #If the first element of the tuple is already in the dictionary and the second element is different, then it is not a function
        #The second condition is for making sure duplicates are not counted
        if elem[0] in vals and vals[elem[0]] != elem[1]:
            #Return false if the condition is met
            return False
        #Add the first element of the tuple as a key and the second element as the value
        vals[elem[0]] = elem[1]
    
    #If the function has not returned false yet, then it is a function therefore return true
    return True

def injective(A, B, f):
    '''
    Inputs: A, B, f (A and B are sets, f is a list of tuples)
    Note: A and B are unused in this function
    Output: True if f is injective, False otherwise
    Function: Tests if f is injective` 
    '''
    #First make an empty dictionary
    vals = dict()

    #Loop through each element in f
    for elem in f:
        #If the second element of the tuple is already in the dictionary and the first element is different, then it is not injective
        #The second condition is for making sure duplicates are not counted
        if elem[1] in vals and vals[elem[1]] != elem [0]:
            #Return false if the condition is met
            return False
        #Add the second element of the tuple as a key and the first element as the value
        vals[elem[1]] = elem[0]
    
    #If the function has not returned false yet, then it is injective therefore return true
    return True


def surjective(A, B, f):
    '''
    Inputs: A, B, f (A and B are sets, f is a list of tuples)
    Note: A is unused in this function
    Output: True if f is surjective, False otherwise
    Function: Tests if f is surjective
    '''

    #Loop through each element in f
    for elem in f:
        #If the second element of the tuple is in B, then remove it from B
        if elem[1] in B:
            #Remove the element second element of the tuple from B
            B.remove(elem[1])
    
    #If B is empty, then it is surjective therefore return true otherwise return false
    return len(B) == 0

def bijective(A, B, f):
    '''
    Inputs: A, B, f (A and B are sets, f is a list of tuples)
    Output: True if f is bijective, False otherwise
    Function: Tests if f is bijective
    '''

    #Return true if the function is injective and surjective otherwise return false
    return injective(A, B, f) and surjective(A, B, f)

def inv(A, B, f):
    '''
    Inputs: A, B, f (A and B are sets, f is a list of tuples)
    Note: A and B are unused in this function
    Output: The inverse of f
    Function: Finds the inverse of f
    '''

    #Return a set of tuples with the first and second element of each tuple swapped
    return {(elem[1], elem[0]) for elem in f}


def q1():
    
    #List of test inputs (they are also numbered)
    test_inputs = [
        ({"a","b","c","d"}, {"v","w","x","y","z"}, {("a","z"),("b","y"),("c","x"),("d","w")}),  #0
        ({"a","b","c","d"}, {"x","y","z"}, {("a","z"),("b","y"),("c","x"),("d","z")}),          #1
        ({"a","b","c","d"}, {"w","x","y","z"}, {("a","z"),("b","y"),("c","x"),("d","w")}),      #2
        ({"a","b","c","d"}, {1,2,3,4,5}, {("a",4),("b",5),("c",1),("d",3)}),                    #3
        ({"a","b","c"}, {1,2,3,4}, {("a",3),("b",4),("c",1)}),                                  #4
        ({"a","b","c","d"}, {1,2,3}, {("a",2),("b",1),("c",3),("d",2)}),                        #5
        ({"a","b","c","d"}, {1,2,3,4}, {("a",4),("b",1),("c",3),("d",2)}),                      #6
        ({"a","b","c","d"}, {1,2,3,4}, {("a",2),("b",1),("c",2),("d",3)}),                      #7
        ({"a","b","c"}, {1,2,3,4}, {("a",2),("b",1),("a",4),("c",3)})                           #8
    ]

    #Loop through each test input
    for a,s,d in test_inputs:
        #Print the test input
        print(f"A = {a} B = {s} f = {d}")


        if is_func(a,s,d):
            #If it is a function, then print that it is a function 
            print("Is a function")
        else:
            #If it is not a function, then print that it is not a function and continue to the next test input
            print("Not a function therefore not injective, surjective or bijective")
            continue

        #Print if it is injective, surjective and bijective or not
        if injective(a,s,d):
            print("Is injective")
        else:
            print("Not injective")
        
        if surjective(a,s,d):
            print("Is surjective")
        else:
            print("Not surjective")
        
        if bijective(a,s,d):
            #
            print("Is bijective", end= ' ')
            print(f"Inverse of f is {inv(a,s,d)}")
        else:
            print("Not bijective therefore no inverse")

def gcd(num1, num2):
    steps = []
    final_gcd = 1
    if num2 > num1:
        num1, num2 = num2, num1
    
    def recursive(num1, num2):
        nonlocal final_gcd
        if num2 == 0:
            return num1

        steps.append(f"{num1}/{num2} = {num1//num2} R {num1%num2}")
        final_gcd = num2

        return recursive(num2, num1%num2)
    
    recursive(num1, num2)
    return steps, final_gcd

def q2():
    pairs = [(414, 662), (6, 14), (24, 36), (12, 42), (252, 198)]

    for a,b in pairs:
        print(f"Steps for gcd({a},{b})")
        result = gcd(a,b)
        for step in result[0]:
            print(step)
        print(f"GCD{(a, b)} = {result[1]}")
        print()


# q2()


result = gcd(252, 198)

steps = result[0]

def bezout_steps(a, b):
    '''
    Inputs: a, b (integers)
    Output: s, t (integers)
    Function: Finds the linear combination of a and b that equals their gcd and prints the steps
    '''

    #Make sure a is greater than b, if not then swap them
    if a < b:
        a, b = b, a
    
    #Initialize the steps list as well as r
    r = 0
    steps = []

    #Printing in the product sum format
    print("Product Sum format: ")

    #Get the steps for the gcd of a and b
    #Loop until b is 0
    while b > 0:

        #Get the quotient and remainder of a and b
        q, r = divmod(a, b)
        #Add the step to the steps list
        steps.append([a, b, q, r])
        print(f"{a} = {b}*{q} + {r}")
        #Set a to b and b to r
        a, b = b, r

    #Start of Euclid backwards format
    print("\nEuclid backwards format: ")
    #Remove the last step because it is 0 and reverse the list
    steps.pop()
    steps = steps[::-1]

    #The final step is the first step in the list since it is reversed
    final = steps[0]
    #Set s to 1
    s = 1

    #Set the GCD to the remainder of the final step, this is the final gcd and won't change
    gcd = final[3]

    #Set the final a, b and q to the thier respective values in the final step. They will change the name is misleading
    final_a = final[0]
    final_b = final[1]
    final_q = final[2]


    #Loop through each step except the first one, the vars in the first step are labeled a, b, t,r respectively
    for a, b, t, r in steps[1:]:

        #Print the step in the form of the equation gcd = s*a - q*b
        print(f"{gcd} = {s} * {final_a} - {final_q} * {final_b}")

        #If the remainder is equal to the final b, then set the index to 1, if the remainder is equal to the final a, then set the index to 0, otherwise set the index to -1 (this is for error checking)
        index = 1 if final_b == r else 0 if final_a == r else -1


        #The index tells us which part of the eq to change
        if index == 1:
            #If index is 1 (the remainder is equal to the final b), then 
            #Print the step in the form of the equation gcd = s*a - q*(a-t*b)
            print(f"{gcd} = {s} * {final_a} - {final_q} * ({a}-{t}*{b})")

            #Set s to equal final_q*t+s and final_b to a
            s = final_q*t+s
            final_b = a
        elif index == 0:
            #If index is 0 (the remainder is equal to the final a), then
            #Print the step in the form of the equation gcd = s*(a-t*b) - q*b
            print(f"{gcd} = {s} * ({a}-{t}*{b}) - {final_q} * {final_b}")

            #In this case we don't need to change s, but we do need to change final_a to s*t+final_q and final_a to a
            final_q = s*t + final_q
            final_a = a    

    #Print the final step in the form of the equation gcd = s*a - q*b
    print(f"{gcd} = {s} * {final_a} - {final_q} * {final_b}")

    #Return s and -q since the equation is gcd = s*a - q*b and we have been typing out the - sign
    return s, -final_q

def q3():

    #List of test inputs
    pairs = (414, 662), (6, 14),  (24, 36), (12, 42), (252, 198)
    letter = ["a", "b", "c", "d", "e"]
    #Loop through each test input
    for i, pair in enumerate(pairs):
        print(f'3{letter[i]}: ')
        bezout_steps(pair[0], pair[1])
        print("\n")


def main():
    print("Question 1:")
    q1()
    
    print("\nQuestion 2:")
    q2()
    print("\nQuestion 3:")
    q3()


main()