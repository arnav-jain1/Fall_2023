#include <iostream>
#include "q2.h"
int main() {

    q1 *qestion1 = new q1(); //Create a new q1 object
    std::cout << std::boolalpha << "Question 1a. " << qestion1->q1a() << std::endl; //Prints q1a and output of function q1a
    std::cout << std::boolalpha << "Question 1b. " << qestion1->q1b() << std::endl; //Prints q1b and output of function q1b
    std::cout << std::boolalpha << "Question 1c. " << qestion1->q1c() << std::endl; //Prints q1c and output of function q1c
    std::cout << std::boolalpha << "Question 1d. " << qestion1->q1d() << std::endl; //Prints q1d and output of function q1d
    std::cout << std::boolalpha << "Question 1e. !Ex: P(x): " << qestion1->q1ep1() << " Ax: !P(x): " << qestion1->q1ep2() << std::endl; //Prints q1ep1 and output of function q1ep1, then prints q1ep2 and output of function q1ep2
    std::cout << "Since both are the same, the De Morgan's law holds." << std::endl; //Prints that De Morgan's law holds
    std::cout << std::boolalpha << "Question 1f. !Ax: P(x): " << qestion1->q1fp1() << " Ex: !P(x): " << qestion1->q1fp2() << std::endl; //Prints q1fp1 and output of function q1fp1, then prints q1fp2 and output of function q1fp2
    std::cout << "Since both are the same, the De Morgan's second law holds." << std::endl; //Prints that De Morgan's second law holds
    std::cout << std::endl; //Prints a new line



    q2 *qestion2 = new q2(); //Create a new q2 object

    std::cout << std::boolalpha <<  "Question 2a. " << qestion2->AxAy() << std::endl; //Prints q2a and output of function AxAy
    std::cout << std::boolalpha << "Question 2b. " << qestion2->AxEy() << std::endl; //Prints q2b and output of function AxEy
    std::cout << std::boolalpha << "Question 2c. " << qestion2->AyEx() << std::endl; //Prints q2c and output of function AyEx
    std::cout << std::boolalpha << "Question 2d. " << qestion2->ExAy() << std::endl; //Prints q2d and output of function ExAy
    std::cout << std::boolalpha << "Question 2e. " << qestion2->EyAx() << std::endl; //Prints q2e and output of function EyAx
    std::cout << std::boolalpha << "Question 2f. " << qestion2->ExEy() << std::endl; //Prints q2f and output of function ExEy
    delete qestion2; //Delete the q2 object

    return 0;
}