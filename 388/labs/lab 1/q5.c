#include <stdio.h>

int main() {
    int size = 10; //Sets the size of the array to 10
    int arr[10] = {2, 3, 1, 7, 3, 3, 2, 9, 1, 3}; //Creates an array of size 10 with the given numbers
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