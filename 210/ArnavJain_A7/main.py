import math

def distOdistB(num1, num2):
    return math.comb(num1, num2)
def indisOdistB(num1, num2):
    return math.comb(num1+num2-1, num1)

def q1():
    ex8 = "Example 8: How many ways are there to deal 5-card poker hands from a 52 card deck to each of the four players"
    total = 1
    for num in range(0, 4):
        total *= distOdistB(52-5*num, 5)
        print(52-5*num)
    print(total)

def q2():
    ex9 =" Example 9: How many ways are there to place 10 indistinguishable balls into 8 distinguishable bins?"
    answer = indisOdistB(10, 8)
    print(answer)

q2()