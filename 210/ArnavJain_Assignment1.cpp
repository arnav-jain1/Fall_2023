/*Prolouge
    *Author: Arnav Jain
    *Date: 8/26/23
    *Name: EECS 210 Assignment 1
    *Desc: C++ code for demonstrating different common laws as well as boolean algebera operators (and, or, implication, etc)
    *Inputs: None
    *Outputs: Prints Truth tables for various laws (Demorgan, associative) as well as different boolean alg equivalencies
    *Collaborators: Just me
    *Other sources: ChatGPT for one instance of ranged based for loops as well as commenting guide, did not make comments but showed me what should be there

    *NOTE: Assume author of code was me unless stated otherwise
*/


#include "iostream"
//Func declarations
void demorganFirst(bool x, bool y);
void demorganSecond(bool x, bool y);
void printer(void (*func)(bool,bool));
void printer(void (*func)(bool, bool, bool));
void associative1(bool x, bool y, bool z); 
void associative2(bool x, bool y, bool z);
bool implication(bool x, bool y);
void q5(bool x, bool y, bool z);
void q6(bool x, bool y);


int main() {
    /*Prolouge
     *Inputs: None
     *Outputs: Nothing
     *Function: Main function that prints the header for truth tables and then calls the respective function
    */
    std::cout << "p\tq\t!(p*q)\t(!p)+(!q)" << std::endl; //Header for q1
    printer(demorganFirst); //Calls printer function with de morgan's first law
    std::cout << std::endl << "p\tq\t!(p+q)\t(!p)*(!q)" << std::endl;//Header for q2
    printer(demorganSecond); //Calls printer with demorgan's second law
    std::cout << std::endl << "p\tq\tr\t((p*q)*r) (p*(q*r))" << std::endl; //Header for q3
    printer(associative1); //Calls printer for associative property with ands
    std::cout << std::endl << "p\tq\tr\t((p+q)+r) (p+(q+r))" << std::endl; // Header for q4
    printer(associative2); //Calls printer for associative property with ors
    std::cout << std::endl << "p\tq\tr\t[(p+q)*(p->r)*(q->r)]->r T" << std::endl; // Header for q5
    printer(q5); //Calls printer for boolean logic in q5
    std::cout << std::endl << "p\tq\tp<->q\t(p->q)*(p->q)" << std::endl; // Header for q6
    printer(q6); //Calls printer for boolean logic in q6
    return 0;
}

void printer(void (*func)(bool, bool)) {
    /*Prolouge
     *Inputs: a function that has 2 bools as its parameters
     *Outputs: Nothing
     *Function: Calls other functions with all possible t/f combinations with 2 vars
    */
    bool values[] = {true, false}; //Stack allocated array that has true and false as its values
    for (bool val1 : values) { //2 nested for loops that go through the array in order to create the truth table effeciently
        for (bool val2 : values) { //For loop uses range based loop so it goes through each element (chat GPT)
            func(val1, val2); //Calls the passed in function with t/f
        }
    }
}

void printer(void (*func)(bool, bool, bool)) {
    /*Prolouge
     *Inputs: a function that has 3 bools as its parameters
     *Outputs: Nothing
     *Function: Calls other functions with all possible t/f combinations with 3 vars
    */
    bool values[] = {true, false};
    for (bool val1 : values) { //Same as before, but with 3 nested for loops since there are now 3 variables
        for (bool val2 : values) {
            for (bool val3 : values) {
                func(val1, val2, val3); //Calls passed in func
            }
        }
    }
}

void demorganFirst(bool x, bool y) {
    /*Prolouge
     *Inputs: 2 bools: x,y
     *Outputs: Nothing
     *Function: printing a truth table De Morgan's first law
    */
    //Prints the value of x, y then outcome of not(x and y) then outcome of (not x) or (not y). All of which is seperated by tabs
    std::cout << x << "\t" << y << "\t" << !(x&&y) << "\t" << (!x||!y) << std::endl; }
void demorganSecond(bool x, bool y) {
    /*Prolouge
     *Inputs: 2 bools: x,y
     *Outputs: Nothing
     *Function: printing a truth table De Morgan's second law
    */
    // Prints value of x, y, then outcome of not(x or y) then outcome of (not x) and (not y). All seperated by tabs
    std::cout << x << "\t" << y << "\t" << !(x||y) << "\t" << (!x&&!y) << std::endl;}
void associative1(bool x, bool y, bool z) {
    /*Prolouge
     *Inputs: 3 bools: x,y,z
     *Outputs: Nothing
     *Function: printing a truth table for associate property with ands
    */
    // Prints value of x,y,z then outcome of ((x and y) and z) then outcome of (x and (y and z))
    std::cout << x << "\t" << y << "\t" << z << "\t" << ((x&&y)&&z) << "\t" << (x&&(y&&z)) << std::endl; }
void associative2(bool x, bool y, bool z) {
    /*Prolouge
     *Inputs: 3 bools: x,y,z
     *Outputs: Nothing
     *Function: printing a truth table for associate property with ors
    */
    // Prints value of x,y,z then outcome of ((x or y) or z) then outcome of (x or (y or z))
    std::cout << x << "\t" << y << "\t" << z << "\t" << ((x||y)||z) << "\t" << (x||(y||z)) << std::endl; }
void q5(bool x, bool y, bool z){
    /*Prolouge
     *Inputs: 3 bools: x,y,z
     *Outputs: Nothing
     *Function: printing a truth table for the function listed in q5
    */
    // Prints x, y, z, then [(p+q)*(p->r)*(q->r)]->r and lastly prints true because the logic will always be true. In order to do all implications, it passes to implication func
    std::cout << x << "\t" << y << "\t" << z << "\t" << implication(((x||y)&&(implication(x, z))&&(implication(y, z))), z) << "\t" << true << std::endl;}
void q6(bool x, bool y) {
    /*Prolouge
     *Inputs: 2 bools: x,y
     *Outputs: Nothing
     *Function: printing a truth table for the function listed in q6
    */
    // Prints x, y then p<->q then (p->q)*(p->q) all seperated by tabs. In order to do implications it passes it to the function and to do
    //biconditional, == is used because biconditional is when both vars are the same
    std::cout << x << "\t" << y << "\t" << (x == y) << "\t" << ((implication(x,y))&&(implication(y,x)))<< std::endl;}

bool implication(bool x , bool y) {
    /*Prolouge
     *Inputs: 2 bools: x,y
     *Outputs: implication of inputs
     *Function: returning the implication of the 2 bools
    */
    return (!x || y); }