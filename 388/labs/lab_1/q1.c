#include <stdio.h>

int main() {
    //Takes in 3 vars, an int, a char, and another int, and performs the operation on the two ints
    int input1; 
    int input2;
    char operand;
    printf("Enter an integer, an operand, and then another integer like this: 1+3 \n");
    scanf("%d %c %d", &input1, &operand, &input2);
    
    //Switch statement to determine which operation to perform
    switch (operand) {
      case '/':
        printf("Quotient for %d and %d is %.2f", input1, input2, (float)input1/input2); //Casts the int to a float to get a decimal then print the quotient
        break;
      case '+':
        printf("Sum for %d and %d is %d", input1, input2, input1+input2); //Prints the sum of the two ints
        break;
      case '-':
        printf("Difference for %d and %d is %d", input1, input2, input1-input2); //Prints the difference of the two ints
        break;
      case '*':
        printf("Product for %d and %d is %d", input1, input2, input1*input2); //Prints the product of the two ints
        break;
      default:
        printf("Invalid operand entered"); //Default switch case for invalid input
        break;
    }
    printf("\n"); //Prints a new line for formatting
    return 0;
} 
