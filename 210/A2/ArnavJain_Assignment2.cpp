#include <iostream>
#include "q2.h"
int main() {

    q1 *qestion1 = new q1(); //Create a new q1 object
    std::cout << std::boolalpha << "Question 1a. " << qestion1->q1a() << std::endl;
    std::cout << std::boolalpha << "Question 1b. " << qestion1->q1b() << std::endl;
    std::cout << std::boolalpha << "Question 1c. " << qestion1->q1c() << std::endl;
    std::cout << std::boolalpha << "Question 1d. " << qestion1->q1d() << std::endl;
    std::cout << std::boolalpha << "Question 1e. !Ex: P(x): " << qestion1->q1ep1() << " Ax: !P(x): " << qestion1->q1ep2() << std::endl;
    std::cout << "Since both are the same, the De Morgan's law holds." << std::endl;
    std::cout << std::boolalpha << "Question 1f. !Ax: P(x): " << qestion1->q1fp1() << " Ex: !P(x): " << qestion1->q1fp2() << std::endl;
    std::cout << "Since both are the same, the De Morgan's second law holds." << std::endl;
    std::cout << std::endl;



    q2 *qestion2 = new q2(); //Create a new q2 object

    std::cout << std::boolalpha <<  "Question 2a. " << qestion2->AxAy() << std::endl;
    std::cout << std::boolalpha << "Question 2b. " << qestion2->AxEy() << std::endl;
    std::cout << std::boolalpha << "Question 2c. " << qestion2->AyEx() << std::endl;
    std::cout << std::boolalpha << "Question 2d. " << qestion2->ExAy() << std::endl;
    std::cout << std::boolalpha << "Question 2e. " << qestion2->EyAx() << std::endl;
    std::cout << std::boolalpha << "Question 2f. " << qestion2->ExEy() << std::endl;
    delete qestion2; //Delete the q2 object

    return 0;
}