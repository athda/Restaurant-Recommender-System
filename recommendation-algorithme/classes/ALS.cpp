//
// Created by ismgh on 03/01/2021.
//
#include "ALS.h"
#include <Eigen/Dense>
#include <Eigen/SparseCore>
#include <iostream>
using Eigen::MatrixXd;
/*constructeur*/
ALS::ALS(int Number_users,int Number_items,int Dimention_vector,int Iterations,float lambda){
    //initialisation of parameters
    this->Number_users=Number_users;
    this ->Number_items=Number_items;
    this->Dimention_vector=Dimention_vector;
    this->Iterations=Iterations;
    this->lambda=lambda;
}
/* initialising the recommendation problem*/
void  ALS::initialize(){
    allocation();
    U=MatrixXd::Random(Number_users, Dimention_vector);//users matrix initialized with random values
    I=MatrixXd::Random(Number_items, Dimention_vector);//iteams matrix initialized with random values
    for (int i=0;i<Number_users;i++)
        for (int j=0;j<Number_items;j++)
            std::cin >> Rating_Matrix[i][j];
}
/* allocating the rating matrix */
void  ALS::allocation(){
    Rating_Matrix= (float **)(malloc(sizeof(float) * Number_users ));//allocation
    for (int i=0;i<Number_users;i++) Rating_Matrix[i]=(float *)(malloc(sizeof(float) * Number_items));
}
/* computing U and V */
void ALS::compute(){
    initialize();//initialise the feed back matrix
    for (int t = 0; t < Iterations; ++t) {
        computeU();
        computeI();
    }
}
void ALS::computeU() {// compute the new U
    for (int u = 0; u < Number_users; ++u) U.row(u)=computeUu(u);
}
void ALS::computeI() {// compute the new I
    for (int i = 0; i < Number_items; ++i) I.row(i)=computeIi(i);
}
MatrixXd ALS::computeUu(int u){// compute the new row u of U <<this can be parallelized>>
    MatrixXd S1=MatrixXd::Zero(Dimention_vector, Dimention_vector);//first sum
    MatrixXd S2=MatrixXd::Zero(Dimention_vector, 1);//second sum
    for (int i = 0; i < Number_items; ++i) {
        if(Rating_Matrix[u][i]>0)
        {
            S1+=I.row(i).transpose()*I.row(i)+ MatrixXd::Identity(Dimention_vector, Dimention_vector) * lambda;
            S2+=Rating_Matrix[u][i]*I.row(i).transpose();
        }
    }
    return (S1.inverse()*S2).transpose();
}
MatrixXd ALS::computeIi(int i){// compute the new row i of I <<this can be parallelized>>
    MatrixXd S1=MatrixXd::Zero(Dimention_vector, Dimention_vector);//first sum
    MatrixXd S2=MatrixXd::Zero(Dimention_vector, 1);//second sum
    for (int u = 0; u < Number_users; ++u) {
        if(Rating_Matrix[u][i]>0) {
            S1 += U.row(i).transpose() * U.row(i) + MatrixXd::Identity(Dimention_vector, Dimention_vector) * lambda;
            S2 += Rating_Matrix[u][i] * U.row(i).transpose();
        }
    }
    return (S1.inverse()*S2).transpose();
}
/*getters*/
Eigen::MatrixXd ALS::getU() {//get matrix of users
    return U;
}
Eigen::MatrixXd ALS::getI() {//get matrix of items
    return I;
}
/*setters*/
void ALS::setDimention_vector(int Dimention_vector){
    this->Dimention_vector=Dimention_vector;
}
void ALS::setIterations(int Iterations){
    this->Iterations=Iterations;
}
void ALS::setlambda(int lambda){
    this->lambda=lambda;
}