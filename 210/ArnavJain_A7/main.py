import math

def distOdistB(num1, num2):
    '''
    inputs: num1, num2
    outputs: combination of num1 and num2
    function: a function for calculating the possibilities of distinguishable objects into distinguishable bins (done via the combination function)
    '''
    return math.comb(num1, num2)
def indisOdistB(num1, num2):
    '''
    inputs: num1, num2
    outputs: Probability based on the function
    function: a function for calculating the possibilities of indistinguishable objects into distinguishable bins (done via the combination function)
    '''
    #The formula is C(n+r-1, r) which is what is being used here
    return math.comb(num1+num2-1, num1)
def distOindisB(num1, num2):
    '''
    inputs: num1, num2
    outputs: total
    function: a function for calculating the possibilities of distinguishable objects into indistinguishable bins (done via the stirling function)
    Help from: https://rosettacode.org/wiki/Stirling_numbers_of_the_second_kind#Java
    '''
    #Total is the total number of ways to put num1 objects into num2 indistinguishable bins
    total = 0

    def stirling(num1, num2):
        ''''''

        #Assume that num1 is the number of objects and num2 is the number of indistinguishable boxes
        if num1 == 0 and num2 == 0:
            #Base case, only one way to put 0 objects into 0 boxes
            return 1
        if num1 == 0:
            #Base case, no way to put 0 objects into any number of boxes
            return 0
        if num2 == 0:
            #Base case, no way to put any number of objects into 0 boxes
            return 0
        if num1 == num2:
            #Base case, only one way to put n objects into n boxes
            return 1
        if num1 < num2:
            #Base case, no way to put n objects into more than m boxes where n < m
            return 0
        
        #Based on the formula S(n, k) = k*S(n-1, k) + S(n-1, k-1)
        #What this formula is saying is that the number of ways to put n objects into k boxes is equal to k*(the number of ways to put n-1 objects into k boxes) + the number of ways to put n-1 objects into k-1 boxes
        # Recursive case
        return num2 * stirling(num1-1, num2) + stirling(num1-1, num2-1) 

    #This while loop is used to add up all the possible ways to put num1 objects into num2 indistinguishable boxes
    while (num2 >= 1):
        # You sum the total number of ways to put num1 objects into num2 indistinguishable boxes for all values of num2 from given num2 to 1 (inclusive)
        total += stirling(num1, num2)
        num2 -= 1
    
    #Return Total
    return total

def indistOindistB(num1, num2):
    '''
    Inputs: num1, num2
    Outputs: The number of ways to put num1 indistinguishable objects into num2 indistinguishable bins
    Function: A function for calculating the possibilities of indistinguishable objects into indistinguishable bins (done via the function P on the lecture slides)
    '''
    def P(num1, num2):
        # This function is based on the function P on the lecture slides
        
        # Base case: If num1 is 0, there is only one way to put 0 indistinguishable objects into n indistinguishable bins
        if num1 == 0:
            return 1
        # Base case: If num2 is 0, there is no way to put n indistinguishable objects into 0 indistinguishable bins (unless n is also 0 but that is covered by the previous base case), num1 cannot be less than 0 if it is return 0
        if num2 == 0 or num1 < 0:
            return 0
        
        # Recursive case: Based on the formula P(n, k) = P(n-k, k) + P(n, k-1) as shown on the lecture slides
        return P(num1-num2, num2) + P(num1, num2-1)


    # Return the function
    return P(num1, num2)

def q1():
    ex8 = "Example 8: How many ways are there to deal 5-card poker hands from a 52 card deck to each of the four players"
    total = 1
    for num in range(0, 4):
        total *= distOdistB(52-5*num, 5)
    print(ex8)
    print(total)

    q1b = "Question 1b: A professor packs her collection of 40 issues of a mathematics journal in four boxes with 10 issues per box. How many ways can she distribute the journals if each box is numbered, so that they are distinguishable?"
    print(q1b)
    total = 1
    for num in range(0, 4):
        total *= distOdistB(40-10*num, 10)
    print(total) 

def q2():
    ex9 ="Example 9: How many ways are there to place 10 indistinguishable balls into 8 distinguishable bins?"
    answer = indisOdistB(10, 8)
    print(ex9)
    print(answer)

    q2b = "Question 2b: How many ways are there to distribute 12 indistinguishable balls into six distinguishable bins?"
    print(q2b)
    print(indisOdistB(12, 6))

def q3():
    ex10 = "Example 10: How many ways can Anna, Billy, Caitlin, and Danny be placed into three indistinguishable homerooms?"
    print(ex10)
    print(distOindisB(4,3))

    q3b = "Question 3b: How many ways are there to put five temporary employees into four identical offices?"
    print(q3b)
    print(distOindisB(5,4))

def q4():
    ex11 = "Example 11: How many ways can you pack six copies of the same book into four identical boxes?"
    print(ex11)
    print(indistOindistB(6,4))

    q4b = "Question 4b: How many ways are there to distribute five indistinguishable objects into three indistinguishable boxes?"
    print(q4b)
    print(indistOindistB(5,3))


def main():
    q1()
    print()
    q2()
    print()
    q3()
    print()
    q4()

if __name__ == "__main__":
    main()