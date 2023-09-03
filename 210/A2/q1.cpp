#include "q2.h" //Include the header file


//Functions for question 1
q1::q1() 
{
    //No arg constructor
    //Constructor that creates the object and initializes the domain var
    const double* domain = new const double[10]{1,2,4,5,6,7,8,9,10}; //Domain of the function
}

q1::~q1()
{
    //Destructor
    delete[] domain; //Delete constructor that deletes the domain
}

bool q1::P1(double x)
{
    //Inputs: x and y (double)
    //Output: bool
    //Function that returns true if x<2
    return x < 2;
}

bool q1::Q1(double x)
{
    //Inputs: x and y (double)
    //Output: bool
    //Function that returns true if x>7
    return x > 7;
}

bool q1::P2(double x)
{
    //Inputs: x and y (double)
    //Output: bool
    //Function that returns true if x<5
    return x < 5;
}

bool q1::q1a()
{
    //Inputs: None
    //Output: bool
    //Function: There exists at least one value of x for which x is less than 2.
    for (int i = 0; i < 10; i++)
    {
        if (P1(domain[i]))
        {
            return true;
        }
    }
    return false;
}

bool q1::q1b()
{
    //Inputs: None
    //Output: bool
    //Function: Every value of x is less than 2.
    for (int i = 0; i < 10; i++)
    {
        if (!P1(domain[i]))
        {
            return false;
        }
    }
    return true;
}

bool q1::q1c()
{
    //Inputs: None
    //Output: bool
    //Function: There exists at least one value of x for which x is either less than 2 or greater than 7.
    for (int i = 0; i < 10; i++)
    {
        if (P1(domain[i]) || Q1(domain[i]))
        {
            return true;
        }
    }
    return false;
}


bool q1::q1d()
{
    //Inputs: None
    //Output: bool
    //Function: For every value of x, x is either less than 2 or greater than 7.
    for (int i = 0; i < 10; i++)
    {
        if (!P1(domain[i]) || !Q1(domain[i]))
        {
            return false;
        }
    }
    return true;
}

bool q1::q1ep1()
{
    //Inputs: None
    //Output: bool
    //Function: Show that De Morgan's law holds when dealing with statements involving the existence of some x for which x is less than 5. Part 1 is for !Ex: P(x)
    for (int i = 0; i < 10; i++)
    {
        if (P2(domain[i]))
        {
            return !true; //Return false if there exists a value of x for which x is less than 5, not true is the same as false, written this way because the statement is !(Ex: P(x))
        }
    }
    return !false;
}

bool q1::q1ep2()
{
    //Inputs: None
    //Output: bool
    //Function: Show that De Morgan's law holds when dealing with statements involving the existence of some x for which x is less than 5. Part 2 is for Ax: !P(x)
    for (int i = 0; i < 10; i++)
    {
        if (!P2(domain[i])) //N!P2 because the statement is !P(x)
        {
            return false; 
        }
    }
    return true; //Return true if for every value of x, x is not less than 5, written this way because the statement is Ax: !P(x)
}

bool q1::q1fp1()
{
    //Inputs: None
    //Output: bool
    //Function: Show that De Morgan's second law holds. Part 1 is for !Ax: P(x) in relation to function x <5
    for (int i = 0; i < 10; i++)
    {
        if (P2(domain[i]))
        {
            return !false; //Not false is used because the statement is !(Ax: P(x))
        }
    }
    return !true; //Return false if for every value of x, x is less than 5, written this way because the statement is !Ax: P(x)
}

bool q1::q1fp2() {
    //Inputs: None
    //Output: bool
    //Function: Show that De Morgan's second law holds. Part 2 is for Ex: !P(x) in relation to function x <5
    for (int i = 0; i < 10; i++)
    {
        if (!P2(domain[i])) //!P2 is used because the statement is Ex: !P(x)
        {
            return true; //Return true if there exists a value of x for which x is not less than 5
        }
    }
    return false;
}