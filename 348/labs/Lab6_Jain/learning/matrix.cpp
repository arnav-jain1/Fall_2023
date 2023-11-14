#include <iostream>
#include <string>
#include "matrix.h"

Matrix::Matrix(int size) 
{
    this->size = new int(size);
    this->matrix = new std::vector<std::vector<int>>(*this->size, std::vector<int>(*this->size));
}

Matrix::~Matrix() 
{
    delete this->size;
    delete this->matrix;
}

void Matrix::setMatrix(int row, int col, int value) 
{
    (*this->matrix)[row][col] = value;
}

int Matrix::getElem(int row, int col)  const
{
    return (*this->matrix)[row][col];
}

int Matrix::getSize() const
{
    return *this->size;
}

void Matrix::printMatrix() const
{
    for (int i = 0; i < *this->size; i++) {
        for (int j = 0; j < *this->size; j++ ) {
            std::cout << (*this->matrix)[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

void Matrix::setSize(int size) 
{
    Matrix::~Matrix();
    this->size = new int(size);
    this->matrix = new std::vector<std::vector<int>>(*this->size, std::vector<int>(*this->size));
}

Matrix::Matrix() {
    this->size = new int(0);
    this->matrix = new std::vector<std::vector<int>>(*this->size, std::vector<int>(*this->size));
}

Matrix Matrix::operator+(const Matrix &rhs) const {

    Matrix result(this->getSize());

    for (int i = 0; i < this->getSize(); i++) {
        for (int j = 0; j < this->getSize(); j++) {
            result.setMatrix(i, j, this->getElem(i,j) + rhs.getElem(i,j));
        }
    }
    return result;
}

Matrix Matrix::operator-(const Matrix &rhs) const {

    Matrix result(this->getSize());

    for (int i = 0; i < this->getSize(); i++) {
        for (int j = 0; j < this->getSize(); j++) {
            result.setMatrix(i, j, this->getElem(i,j) - rhs.getElem(i,j));
        }
    }
    return result;
}

Matrix Matrix::operator*(const Matrix &rhs) const {

    Matrix result(this->getSize());

    for (int i = 0; i < this->getSize(); i++) {
        for (int j = 0; j < this->getSize(); j++) {
            int sum = 0;
            for (int k = 0; k < this->getSize(); k++) {
                sum += this->getElem(i,k) * rhs.getElem(k,j);
            }
            result.setMatrix(i, j, sum);
        }
    }
    return result;
}

std::ostream& operator<<(std::ostream& os, const Matrix &matrix) {
    for (int i = 0; i < matrix.getSize(); i++)
    {
        for (int j = 0; j < matrix.getSize(); j++) {
            os << matrix.getElem(i,j) << ' ';
        }
        os << '\n';
    }
    return os;
}