#include <iostream>
#include <string>
#include <set>
int main() {

    std::set<std::pair<int,int>>* set = new std::set<std::pair<int,int>>();
    set->insert({1,1});
    set->insert({2,2});
    set->insert({3,3});

    std::set<std::pair<int,int>>* set2 = new std::set<std::pair<int,int>>();
    set2->insert({1,1});
    set2->insert({1,2});
    set2->insert({1,3});
    set2->insert({1,4});

    delete[] set;
    delete[] set2;
    return 0;
}