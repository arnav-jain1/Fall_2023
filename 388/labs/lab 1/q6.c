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

    int* min = &arr[0]; //Gets the address of the first element in the array
    int* max = &arr[size-1]; //Gets the address of the last element in the array
    printf("%d", max-min+1); //Prints the difference between the two addresses and adds 1 to account for the first element
    return 0;
}