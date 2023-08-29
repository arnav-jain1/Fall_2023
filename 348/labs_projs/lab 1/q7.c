#include <stdio.h>
#include <math.h>
#include<stdlib.h>
#include <string.h>
int main() {
    //Takes in 3 vars, an int, a char, and another int, and performs the operation on the two ints
    float input1; 
    float input2;
    char operand[10];
    printf("Enter 2 numbers \n");
    scanf("%f %f", &input1, &input2);
    fflush(stdin);
    printf("Enter an operand (type sqrt for square root, ciel for cieling, flr for floor, exp for exponent, and (a+b)^2 for (a+b)^2)\n");
    scanf("%s", operand);
    
    //If statements to determine which operation to perform based on the operand. String compare is used to compare the strings
    if (strcmp(operand, "/") == 0 ) {
        printf("Quotient for %.2f and %.2f is %.2f", input1, input2, input1/input2); //Prints the quotient of the two floats
    } else if (strcmp(operand, "+") == 0) {
        printf("Sum for %.2f and %.2f is %.2f", input1, input2, input1+input2); //Prints the sum of the two floats
    } else if (strcmp(operand, "-") == 0) {
        printf("Difference for %.2f and %.2f is %.2f", input1, input2, input1-input2); //Prints the difference of the two floats
    } else if (strcmp(operand, "*") == 0) {
        printf("Product for %.2f and %.2f is %.2f", input1, input2, input1*input2); //Prints the product of the two floats
    } else if (strcmp(operand, "sqrt") == 0) {
        printf("Square root of %.2f is %.2f", input1, sqrt(input1)); //Prints the square root of the first float
    } else if (strcmp(operand, "ciel") == 0) {
        printf("Cieling of %.2f is %.2f", input1, ceil(input1)); //Prints the cieling of the first float
    } else if (strcmp(operand, "flr") == 0) { 
        printf("Floor of %.2f is %.2f", input1, floor(input1)); //Prints the floor of the first float
    } else if (strcmp(operand, "exp") == 0) {
        printf("%.2f to the %.2f is %.2f", input1, input2, pow(input1, input2)); //Prints the power of the first float the second float
    } else if (strcmp(operand, "(a+b)^2") == 0) {
        printf("(%.2f + %.2f)^2 is %.2f", input1, input2, pow(input1+input2, 2)); //Prints the square of the sum of the two floats
    } else {
        printf("Invalid operand entered: %s", operand); //Prints if the operand is invalid
    }

    printf("\n"); //Prints a new line for formatting
    return 0;
} 