#ifndef q1_H
#define q1_H
#include <iostream> 
#include <set>

class q1
{
    private:
        std::set<std::pair<int,int>>* set1; //Pointer to set 1
        std::set<std::pair<int,int>>* set2; //Pointer to set 2


    
    public:
        ~q1(); //Destructor
        q1(); //No arg constructor

};
#endif