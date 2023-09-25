#include "q1.h"
q1::q1() {
    set1 = new std::set<std::pair<int,int>>();
    set1->insert({1,1});
    set1->insert({2,2});
    set1->insert({3,3});

    set2 = new std::set<std::pair<int,int>>();
    set2->insert({1,1});
    set2->insert({1,2});
    set2->insert({1,3});
    set2->insert({1,4});

}

q1::~q1() {
    delete set1;
    delete set2;
}