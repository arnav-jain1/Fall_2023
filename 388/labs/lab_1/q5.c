#include <stdio.h>

int main() {
    int size; 
    printf("Enter the size of the array: "); //Gets the size of the array so it can make an array from the input
    scanf("%d", &size);
    int arr[size];
    printf("Enter the numbers you want in the array seperated by a space \n");
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]); //Keeps scanning depending on the size of the array and puts the numbers in the array
    }

    //Old code for testing
    // int size = 10; //Sets the size of the array to 10
    // int arr[10] = {2, 3, 1, 7, 3, 3, 2, 9, 1, 3}; //Creates an array of size 10 with the given numbers
    
    
    int duplicates = 0; //Sets the number of repeated numbers to 0
    for (int i = 0; i < size; i++) { //Loops through every num in the array
        for (int j = i+1; j < size; j++) {
            //Nested for loop that loops through every num after the current num
            if (arr[i] == arr[j]) {
                //Increase the duplicate count if the two numbers are the same
                duplicates++;
                break; //Breaks out of the loop to avoid double counting
            }
        }
    }
    printf("%d", duplicates); //Prints the number of repeated numbers
    return 0;
}