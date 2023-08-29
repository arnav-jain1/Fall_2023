#include <stdio.h>
#include <stdbool.h>

void hextobi() {
  //Takes in a hex and prints the binary equivalent
  //Answer is stored in an array that is 32 digits long which are all saved as 0 at first
  unsigned int hex;
  int ans[32];
  for (int i = 0; i < 32; i++) {
    //Goes through each digit and sets it to 0
    ans[i] = 0;
  }
  //Gets the input
  printf("Input a hex \n");
  scanf("%x", &hex);
  printf("\n");
  int counter = 31;
  while (hex > 0) {
    //Goes through each digit and sets it to 1 if the remainder is 1. Then divides the hex by 2 and decrements the place
    ans[counter] = hex % 2;
    hex = hex/2;
    counter--;
  }

  for (int i = 0; i < 32; i++) {
    //Prints the answer with a space every 4 digits for formatting
    printf("%d", ans[i]);
    if ((i+1)%4==0) 
      printf(" ");
  }
}

void decToHex() {
  //Takes in a binary as an integer and prints the hex equivalent
  int inp;
  int decimal =0;
  int base = 1, rem;
  printf("Input a binary num\n");
  scanf("%d", &inp);
  while (inp > 0) {
    //Converts the binary to decimal by multiplying each digit by 2^place 
    //And then looks at the next digit until there are no more digits
    rem = inp % 10;
    decimal += rem*base;
    base *=2;
    inp /= 10;
  }
  printf("\n%x\n", decimal);
}
int main() {
  //Asks whether to do binary to hex or hex to decimal
  char input;
  printf("Type 1 if you would like to do binary to hex and 2 if you would like to do hex to decimal \n");
  scanf("%c", &input);
  printf("\n"); //Prints a new line for formatting
  //Switch case to determine which function to call
  switch (input) {
    case '1':
    decToHex(); //Calls the function if input is 1
    break;
    case '2':
    hextobi(); //Calls the function if input is 2
    break;
    default:
    printf("Invalid entry"); //Default case if input is not 1 or 2
  }
  return 0;
} 
