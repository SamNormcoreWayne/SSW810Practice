#include <iostream>

class Rectangle
{
private:
    int label = 1;
    int length = 1;
    int width = 1;
public:
    Rectangle(int a = 1, int b = 1, int c = 1)
    {
        std::cout << "Rectangle constructor." << std::endl;
        this->label = a;
        this->length = b;
        this->width = c;
    }

    int area();
    int perimeter();
};

int Rectangle::area()
{
    return length * width;
}

int Rectangle::perimeter()
{
    return length * 2 + width * 2;
}

class Square : public Rectangle
{
public:
    Square(){}
};

int main()
{
    Rectangle rec= Rectangle();
    Square squ = Square();
    return 1;
}