#include <iostream>
#include <string>

class ListEptError
{
private:
    std::string msg = "";
public:
    ListEptError(std::string msg)
    {
        this->msg = msg;
    }
};

template <typename T>
class Node
{
public:
    T data;
    struct Node<T> *next;
};

template <typename T>
class LinkList
{
private:
    Node<T> *head;
    Node<T> *CurrNode;
public:
    LinkList()
    {
        this->head = nullptr;
        this->CurrNode = nullptr;
    }

    LinkList(int length, T eleVal)
    {
        int i = 0;
        Node<T> *curr = this->head;
        for(i = 0; i < length; ++i)
        {
            curr = new Node<T>;
            curr.value = eleVal;
            curr = curr->next;
            curr->next = nullptr;
        }
        *curr = nullptr;
        delete curr;
    }

    void init();
    void remove();
    T begin();
    T end();
    bool empty();  
};

template <typename T>
void LinkList<T>::init()
{
    this->head = nullptr;
    this->CurrNode = nullptr;
}

template <typename T>
void LinkList<T>::remove()
{
    Node<T> *curr = this->head;
    while(curr->next != nullptr)
        curr = curr->next;
    delete *curr;
}

template <typename T>
T LinkList<T>::begin()
{
    if (this->head)
        return this->head->value;
}

template <typename T>
T LinkList<T>::end()
{

    Node<T>* curr = this->head;
    while(curr->next != nullptr)
        curr = curr->next;
    return curr.value;
}