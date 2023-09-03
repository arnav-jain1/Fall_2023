#ifndef ACCOUNT_H
#define ACCOUNT_H
#include <iostream>
#include <string>

class Account
{
private:
    unsigned int* accountNumber;
    double* balance;
    std::string* ownerName;
public:
    Account(double balance, std::string ownerName);
    Account();
    Account(const Account& orig);
    ~Account();
    void deposit(const double& amount);
    void withdraw(double amount);
    double getBalance();
    int getAccountNumber();
    std::string getOwnerName();
    void setBalance(double balance);

};



#endif // ACCOUNT_H