//
// Created by ismgh on 03/01/2021.
//

#ifndef RECOMENDER_SYSTEME_ALS_H
#define RECOMENDER_SYSTEME_ALS_H
#include <Eigen/SparseCore>
class ALS {
    //attributes
private:
    int Number_users;
    int Number_items;
    int Dimention_vector;
    int Iterations;
    float lambda;//regularisation hyper parameter
    float **Rating_Matrix;
    Eigen::MatrixXd U;//la matrice des utilisateurs
    Eigen::MatrixXd I;//la matrice des utilisateurs
    //functions
public:
    /*constructeur*/
    ALS(int Number_users,int Number_items,int Dimention_vector=4,int Iterations=400,float lambda=0.6);
    /* Compute U and I << users and items matrix*/
    void compute();
    /* getters */
    Eigen::MatrixXd getU();//get matrix of users
    Eigen::MatrixXd getI();//get matrix of items
    /* setters */
    void setDimention_vector(int Dimention_vector);
    void setIterations(int Iterations);
    void setlambda(int lambda);
private:
    /* initialising the feedback matrix*/
    void  initialize();
    /* allocating the rating matrix */
    void  allocation();
    /*computation of U and I */
    void computeU();// compute the new U
    void computeI();// compute the new I
    Eigen::MatrixXd computeUu(int u);// compute the new row u of U <<this can be parallelized>>
    Eigen::MatrixXd computeIi(int i);// compute the new row i of I <<this can be parallelized>>
};


#endif //RECOMENDER_SYSTEME_ALS_H
