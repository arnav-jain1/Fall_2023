#ifndef MATRIX_H
#define MATRIX_H
#include <iostream>
#include <string>
#include <vector>
class Matrix 
{
private:
    int *size;
    std::vector<std::vector<int>> *matrix;

public:

    Matrix(int size);
    Matrix();
    ~Matrix();
    void setMatrix(int row, int col, int value);
    int getElem(int row, int col) const;
    int getSize() const;
    void printMatrix() const;
    void setSize(int size);
    Matrix operator+(const Matrix &rhs) const;
    Matrix operator-(const Matrix &rhs) const;
    Matrix operator*(const Matrix &rhs) const;
    friend std::ostream& operator<<(std::ostream &os, const Matrix &matrix);
}; 

#endif // MATRIX_H