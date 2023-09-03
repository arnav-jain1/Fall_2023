#include "account.h"
#include <iostream>
#include <string>
#include <random>
#include <ctime>
Account::Account(double balance, std::string ownerName)
{
    srand(time(NULL));
    this->balance = new double(balance);
    std::cout << "Account created with balance: " << *(this->balance) << std::endl;
    this->ownerName = new std::string(ownerName);
    this->accountNumber = new unsigned int(rand() % 1000000);
}
Account::Account()
{
    srand(time(NULL));
    this->balance = new double(0);
    std::cout << "Account created with balance: " << *(this->balance) << std::endl;
    this->ownerName = new std::string("");
    this->accountNumber = new unsigned int(rand() % 1000000);
}
Account::Account(const Account& orig)
{
    this->accountNumber = new unsigned int(rand() % 1000000);
    this->balance = new double(*orig.balance);
    this->ownerName = new std::string(*orig.ownerName);
    std::cout << "Account created with balance: " << *(this->balance) << std::endl;
}
Account::~Account()
{
    delete this->balance;
    std::cout << "Account of " << *this->accountNumber << " successfully deleted" << std::endl;
    delete this->accountNumber;
    delete this->ownerName;
}

void Account::deposit(const double& money) 
{
    *(this->balance) += money;
}
double Account::getBalance()
{
    return *this->balance;
}