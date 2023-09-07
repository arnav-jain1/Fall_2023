#include <iostream>
#include "account.h"
int main() {
    Account* acc = new Account(1000, "John Doe");
    acc->deposit(500);
    Account acc2 = Account(*acc);
    acc2.deposit(200);
    std::cout << acc->getBalance() << std::endl;
    std::cout << acc2.getBalance() << std::endl;
    std::cout << std::endl;
    delete acc;
    // delete acc2;
    return 0;
}
