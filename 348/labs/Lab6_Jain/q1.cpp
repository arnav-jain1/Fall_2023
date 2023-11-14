#include "iostream"
#include "fstream"

#define MAX_MATRIX_SIZE 100
#define FILE_PATH "input.txt"
int (*matrix1)[MAX_MATRIX_SIZE] = new int[MAX_MATRIX_SIZE][MAX_MATRIX_SIZE];
int (*matrix2)[MAX_MATRIX_SIZE] = new int[MAX_MATRIX_SIZE][MAX_MATRIX_SIZE];
int* size;


int get_info_from_file();
void print_matrix(int (*matrix)[MAX_MATRIX_SIZE]);
void add_matrix();
void multiply_matrix();
void subtract_matrix();
void delete_all();

int main() {

    if (get_info_from_file() == 1) {
        delete_all();
        return 1;
    }

    std::cout << "Arnav Jain \nLab #6: Matrix Manipulation \n" << std::endl;
    std::cout << "Matrix A: " << std::endl;
    print_matrix(matrix1);
    std::cout << std::endl;


    std::cout << "Matrix B: " << std::endl;
    print_matrix(matrix2);
    std::cout << std::endl;

    std::cout << "Matrix Sum (A + B): " << std::endl;
    add_matrix();
    std::cout << std::endl;

    std::cout << "Matrix Product (A * B): " << std::endl;
    multiply_matrix();
    std::cout << std::endl;

    std::cout << "Matrix Difference (A - B): " << std::endl;
    subtract_matrix();
    std::cout << std::endl;


    delete_all();
    return 0;
}

int get_info_from_file() {

    std::ifstream file(FILE_PATH);

    size = new int;
    if (!file) {
        std::cerr << "Invalid filepath" << std::endl;
        return 1;
    }
    file >> *size;

    char throwaway;

    while (file.get(throwaway) && throwaway != '\n');


    for (int i = 0; i < *size; i++) {
        for (int j = 0; j < *size; j++) {
            file >> matrix1[i][j];
        }
    }
    for (int i = 0; i < *size; i++) {
        for (int j = 0; j < *size; j++) {
            file >> matrix2[i][j];
        }
    }

    return 0;
}

void print_matrix(int (*matrix)[MAX_MATRIX_SIZE]) {
    for (int i = 0; i < *size; i++) {
        for (int j = 0; j < *size; j++ ) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

void add_matrix() {
    for (int i = 0; i < *size; i++) {
        for (int j = 0; j < *size; j++ ) {
            std::cout << matrix1[i][j] + matrix2[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

void multiply_matrix() {

    for (int i = 0; i < *size; i++) {
        for (int j = 0; j < *size; j++ ) {
            int sum = 0;
            for (int k = 0; k < *size; k++) {
                sum += matrix1[i][k] * matrix2[k][j];
            }
            std::cout << sum << " ";
        }
        std::cout << std::endl;
    }
}

void subtract_matrix() {
    for (int i = 0; i < *size; i++) {
        for (int j = 0; j < *size; j++ ) {
            std::cout << matrix1[i][j] - matrix2[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

void delete_all() {
    delete[] matrix1;
    delete[] matrix2;    
    delete size;
}