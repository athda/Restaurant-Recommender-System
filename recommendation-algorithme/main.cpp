#include "classes/ALS.h"//la classe qui va faire la factorisation de la matrice
#include <Eigen/Dense>
#include <Eigen/SparseCore>
#include <iostream>
using Eigen::MatrixXd;
int main(int argc, char** argv) {
    //feedback matrix
    int Number_users=4,Number_items=3,Dimention_vector=3,Iterations=400;
    Dimention_vector=atoi(argv[1]) ;
    ALS algorithme(Number_users,Number_items);
    algorithme.setDimention_vector(Dimention_vector);
    algorithme.compute();
    std::cout << "les restaurant"<< std::endl;
    std::cout << algorithme.getI()<< std::endl;
    std::cout << "les utilisateurs"<< std::endl;
    std::cout << algorithme.getU()<< std::endl;
    std::cout << "approximation de A"<< std::endl;
    std::cout << algorithme.getU()*algorithme.getI().transpose() << std::endl;
    return 0;
}