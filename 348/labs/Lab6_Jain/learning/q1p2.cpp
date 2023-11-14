#include "iostream"
#include "fstream"
#include "vector"
#include "matrix.h"

int get_info_from_file(Matrix* matrix1, Matrix* matrix2);
#define FILE_PATH "input.txt"
int main() {

    Matrix* matrix1 = new Matrix();
    Matrix* matrix2 = new Matrix();

    get_info_from_file(matrix1, matrix2);

    std::cout << "Arnav Jain \nLab #6: Matrix Manipulation \n" << std::endl;
    std::cout << "Matrix A: " << std::endl;
    std::cout << *matrix1 << std::endl;

    std::cout << "Matrix B: " << std::endl;
    std::cout << *matrix2 << std::endl;

    Matrix* matrix3 = new Matrix(*matrix1 + *matrix2);
    std::cout << "Matrix Sum: " << std::endl;
    std::cout << *matrix3 << std::endl;

    Matrix* matrix4 = new Matrix(*matrix1 * *matrix2);
    std::cout << "Matrix Product: " << std::endl;
    std::cout << *matrix4 << std::endl;

    Matrix* matrix5 = new Matrix(*matrix1 - *matrix2);
    std::cout << "Matrix Difference: " << std::endl;
    std::cout << *matrix5 << std::endl;


    delete matrix4;
    delete matrix5;
    delete matrix3;
    delete matrix1;
    delete matrix2;
    return 0;
}

int get_info_from_file(Matrix* matrix1, Matrix* matrix2) {

    std::ifstream file(FILE_PATH);

    int size;
    if (!file) {
        std::cerr << "Invalid filepath" << std::endl;
        return 1;
    }
    file >> size;
    matrix1->setSize(size);
    matrix2->setSize(size);
    char throwaway;

    while (file.get(throwaway) && throwaway != '\n');

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++ ) {
            int value;
            file >> value;
            matrix1->setMatrix(i, j, value);
        }
    }
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++ ) {
            int value;
            file >> value;
            matrix2->setMatrix(i, j, value);
        }
    }

    return 0;
}
