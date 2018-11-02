#include <iostream>
#include <exception>
using namespace std;

int main()
{
    int *b;
    b = new int;
    *b = 4;
    int *a = new int;
    cout << "*a: " << *a << "\n a:" << a << endl;
    a = b;
    cout << "*a: " << *a << "\n a:" << a << endl;
    delete a;
    try
    {
        cout << *b << "\n" << b << endl;
        delete b;
    }
    catch (...)
    {
        cout << "b not exists. " << endl;
    }
}