#ifndef Q2_H // Preprocessor directive to ensure the header is only included once
#define Q2_H
#include <iostream> // Include the iostream library

//Class definition for question 2
class q2 
{
private:
    const double* domain; //Pointer to the domain of the function
    bool function(double x, double y); //Function that returns true if x*y == 1
public:
    ~q2(); //Destructor
    q2(); //No arg constructor
    // Member functions to evaluate different logical propositions
    bool AxAy(); // For all x, for all y, P(x, y) holds
    bool AxEy(); // For all x, there exists y such that P(x, y) holds
    bool AyEx();  // For all y, there exists x such that P(x, y) holds
    bool ExAy();  // There exists x such that for all y, P(x, y) holds
    bool EyAx();  // There exists y such that for all x, P(x, y) holds
    bool ExEy();  // There exists x and y such that P(x, y) holds
};

//Class definition for question 2
class q1
{
private:
    const double* domain; //Pointer to the domain of the function
    bool P1(double x); //Function that returns true if x<2
    bool Q1(double x); //Function that returns true if x>7
    bool P2(double x); //Function that returns true if x<5
public:
    ~q1(); //Destructor
    q1(); //No arg constructor
    // Member functions to evaluate different logical propositions
    bool q1a(); //Function for: There exists at least one value of x for which x is less than 2.
    bool q1b(); //Function for: Every value of x is less than 2.
    bool q1c(); //Function for: There exists at least one value of x for which x is either less than 2 or greater than 7.
    bool q1d(); //Function for: For every value of x, x is either less than 2 or greater than 7.
    bool q1ep1(); //Function for: De Morgan's first law holds. Part 1 is for !Ex: P(x) in relation to function x <5
    bool q1ep2(); //Function for: De Morgan's first law holds. Part 2 is for Ax: !P(x) in relation to function x <5
    
    bool q1fp1(); //Function for: De Morgan's second law holds. Part 1 is for !Ax: P(x) in relation to function x <5
    bool q1fp2(); //Function for: De Morgan's second law holds. Part 2 is for Ex: !P(x) in relation to function x <5
};

#endif // Q2_H