#include <iostream>

template <class T>
class BiNode
{
public:
    T data;
    struct BiNode *leftChild, *rightChild;
};

template <class T>
class BinaryTree
{
private:
    BiNode *Root;
    T value;
    T floor;
public:
    BinaryTree()
    {
        leftChild = NULL；
        rightChild = NULL;
        value = 0;
        floor = 0;
        *Root = value;
    }

    void CreateBiTree()
    {

    }
};