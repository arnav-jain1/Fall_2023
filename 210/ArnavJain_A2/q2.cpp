#include "q2.h" //Include the header file


//Functions for question 2
q2::q2() 
{
    //No arg constructor
    //Constructor that creates the object and initializes the domain var
    domain = new const double[9]{1,2,4,5,10,0.5,0.25,0.2,0.1}; //Domain of the function
}

q2::~q2()
{
    //Destructor
    delete[] domain; //Delete constructor that deletes the domain
}

bool q2::function(double x, double y)
{
    //Inputs: x and y (double)
    //Output: bool
    //Function that returns true if x*y == 1
    return (x*y) == 1;
}

bool q2::AxAy()
{
    //Inputs: None
    //Output: bool
    //Function that returns false if for all x in domain, there exists a y in domain such that x*y != 1
    for (int i =0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            //Two nested for loops that iterate through the domain and check if F returns false
            if (!function(this->domain[i], this->domain[j]))
            {
                return false; //If F returns false then return false
            }
        }
    }
    return true; //If F never returns false then return true
}

bool q2::AxEy()
{
    //Inputs: None
    //Output: bool
    // Description: Checks the truth value of the proposition "For all x, there exists y such that P(x, y) is true".
    // Loop Structure: For each x in the domain, it checks if there is at least one y in the domain making P(x, y) true.
    for (int i=0; i < 9; i++) {
        for (int j=0; j < 9; j++) {
            //If F returns true then break out of the loop and move on to the next x
            if (function(this->domain[i], this->domain[j])) {
                break;
            } else if ((!function(this->domain[i], this->domain[j]) && j == 8)) { 
                //If F returns false and we are at the last y then return false
                return false;
            }
        }
    }
    return true;
}

bool q2::AyEx()
{
    //Inputs: None
    //Output: bool
    // Description: Checks the truth value of the proposition "For all y, there exists x such that P(x, y) is true".
    // Loop Structure: For each y in the domain, it checks if there is at least one x in the domain making P(x, y) true.
    //Essentially the same as previous one since the domain is the same
    for (int j =0; j < 9; j++)
    {
        for (int i = 0; i < 9; i++)
        {
            if (function(this->domain[j], this->domain[i])) {
                break;
            } else if ((!function(this->domain[i], this->domain[j]) && i == 8)) {
                return false;
            }
        }
    }
    return true;
}

bool q2::ExAy()
{
    //Inputs: None
    //Output: bool
    // Description: Checks the truth value of the proposition "There exists x such that for all y, P(x, y) is true".
    // Loop Structure: For each x in the domain, it checks if P(x, y) is true for all y in the domain.
    for (int i =0; i < 9; i++)
    {
        bool allTrue = true; //Boolean that is true if P(x, y) is true for all y, it is initally true because if it is unchanged then it is true
        for (int j = 0; j < 9; j++)
        {
            if (!function(this->domain[i], this->domain[j])) {
                allTrue = false; //If P(x, y) is false then set allTrue to false and break out of the loop
                break;
            } 
        }
        if (allTrue) {
            return true; //If allTrue is true by the end of the second loop, then return true
        }
    }
    return false;
}

bool q2::EyAx()
{
    //Inputs: None
    //Output: bool
    // Description: Checks the truth value of the proposition "There exists y such that for all x, P(x, y) is true".
    // Loop Structure: For each y in the domain, it checks if P(x, y) is true for all x in the domain.
    //Essentially the same as previous one since the domain is the same
    for (int j =0; j < 9; j++)
    {
        bool allTrue = true;
        for (int i = 0; i < 9; i++)
        {
            if (!function(this->domain[i], this->domain[j])) {
                allTrue = false;
                break;
            } 
        }
        if (allTrue) {
            return true;
        }
    }
    return false;
}

bool q2::ExEy()
{
    //Inputs: None
    //Output: bool
    // Description: Checks the truth value of the proposition "There exists x such that there exists y such that P(x, y) is true".
    // Loop Structure: For each x in the domain, it checks if there is at least one y in the domain making P(x, y) true. As long as F is true once, the proposition is true
    for (int i =0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            if (function(this->domain[i], this->domain[j]))
            {
                return true; //If F returns true then return true
            }
        }
    }
    return false;
}


