#include <iostream>
using namespace std;
 
float eps_32(void)
{
    float e = 1.0f;
 
    while (1.0f + e != 1.0f)
        e /= 2.0f;
    return e;
}
 
double eps_64(void)
{
    double e = 1.0;
    double number = 1.0;
 
    while (number + e != number)
        e /= 2.0;
    return e;
}
 
int main(){ 
    cout << "eps 32 bits: " << eps_32() << endl;
    cout << "eps 64 bits: " << eps_64() << endl;
