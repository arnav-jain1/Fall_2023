#include <stdio.h>
#include <stdbool.h>


bool isPrime(int n) {
  //Function for determining if a number is prime
  if (n <= 1) {
    return false; //Case for 0, 1
  } else if (n == 2) {
    return true; //Case for 2
  }


  for (int i = 2; i < n; i++) {
    //Goes through every case from 2 to n-1
    if (n % i == 0) {
      return false; //If n is divisible by any number from 2 to n-1, it is not prime and returns false
    }
  }

  return true; //If n is not divisible by any number from 2 to n-1, it is prime and returns true
}

int main() {
  //Takes one integer input
  int input;
  printf("Enter an integer \n");
  scanf("%d", &input);
  printf("The primes up to that number are: "); //Prints a message for formatting
  for (int i = 0; i <= input; i++)
  //Goes through every number from 0 to the input
  {
    //If it is prime (passes to the function) it prints the number
    if (isPrime(i)) {
      printf("%d, ", i);
    }
  }
    return 0;
} 