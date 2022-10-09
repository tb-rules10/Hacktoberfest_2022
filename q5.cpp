#include<iostream>
#include<math.h>
using namespace std;
int main(){
int a,b,c,d,e;
cout<<"Please enter the coordinates of the point: "<<endl;
cin>>a>>b;
cout<<"Please enter the constant of the equation: "<<endl;
cin>>c>>d>>e;
float num= ((c*a)+(d*b)+e);
float den= sqrt((pow(c,2)+pow(d,2)));
cout<<"The distance between point and line is: "<<(num/den);
}