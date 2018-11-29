#include <iostream>

bool fun()
{
    return true;
}

int main()
{
    bool i = false;
    if(i = fun())
        std::cout << "test." << std::endl;
}