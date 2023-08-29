#include <stdio.h>

int main() {
    //Takes in an int and prints a message based on the value of the int
    int input1;
    printf("Enter your height in cm \n");
    scanf("%d", &input1);
    if (input1 < 160) {
      printf("You are short"); //Prints a message if the input is less than 160
    } else if (input1 < 180) {
      printf("You are medium"); //Prints a message if the input is less than 180
    } else {
      printf("You are tall"); //Prints a message if the input is greater than or equal to 180
    }
    printf("\n"); //Prints a new line for formatting
    return 0;
} 
