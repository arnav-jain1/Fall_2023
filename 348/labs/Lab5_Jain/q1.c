#define FILE_NAME "./input1.txt"


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//Global array
float nums[12];
const char *months[12] = {
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
};


// Function prototypes
int read_file();
float maxfunc(int *index);
float minfunc(float startval, int *index);
float smma(int start, int end);


int main() {
    if (read_file() == 0) {
        exit(1);
    }
    printf("Monthly Sales Report: \n");
    printf("Month        Sales\n");   
    for (int i = 0; i < 12; i++) {
        printf("%-12s $%.2f\n", months[i], nums[i]);
    }
    printf("\nSales Summary: ");
    int index_min = 0;
    int index_max = 0;
    float max = maxfunc(&index_max);
    float min = minfunc(max, &index_min);

    printf("\nMaximum sales: $%.2f (%s)", max, months[index_max]);
    printf("\nMinimum sales: $%.2f (%s)", min, months[index_min]);
    printf("\nAverage sales: $%.2f\n", smma(0, 12));


    printf("\n\nSix-Month Moving Average Report\n");

    for (int i=0; i <= 6; i++) {
        printf("%-12s - %-12s $%.2f\n", months[i], months[i+5], smma(i, i+6));
    }
    printf("\n");

    printf("Sales Report (High to Low)\n");
    high_to_low();

    return 0;
}

int read_file() {

    FILE *file;
    float num;
    int counter = 0;
    file = fopen(FILE_NAME, "r");

    if (file == NULL) {
        printf("Unable to read file\n");
        return 0;
    }
    
    while (fscanf(file, "%f", &num) == 1) {
        nums[counter] = num;
        counter++;
    }

    fclose(file);
    return 1;
}

float maxfunc(int *index) {
    float max = 0;
    for (int i = 0; i < 12; i++) {
        if (max < nums[i]) {
            max = nums[i];
            *index = i;
        }
    }
    return max;
}

float minfunc(float startval, int *index) {
    for (int i = 0; i < 12; i++) {
        if (startval > nums[i]) {
            startval = nums[i];
            *index = i;
        }
    }
    return startval;
}

float smma(int start, int end) {
    float sum = 0;
    for (int i = start; i < end; i++) {
        sum += nums[i];
    }
    sum /= (end - start);
    return sum;
}

int compare(const int *x, const int *y) {
    if (nums[*x] < nums[*y]) return 1;
    if (nums[*x] > nums[*y]) return -1;
    return 0;
}
void high_to_low() {
    int indexes[12] = {0,1,2,3,4,5,6,7,8,9,10,11};
    qsort(indexes, 12, sizeof(int), compare);
    printf("Month        Sales (High to Low)\n");  

    for (int i = 0; i < 12; i++) {
        printf("%-12s $%.2f\n", months[indexes[i]], nums[indexes[i]]);
    }
}
