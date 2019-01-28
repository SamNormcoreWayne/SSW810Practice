#include<iostream>

using namespace std;

template <class T>
class Node
{
private:
    T data;
    Node *next;
};
template <class T>
class LinkList
{
private:
    Node *head == nullptr;
public:
    LinkList(T ele)
    {
        this->head->data = ele;
        this->head->next = nullptr;
    }

    bool isEpt()
    {
        if (this->head == nullptr)
            return TRUE;
        else
            return FALSE;
    }

    void append(T ele)
    {
        Node *newNode = new Node;
        newNode->data = ele;
        newNode->next = nullptr;
        Node *tmpNode = this->head;
        while(tmpNode != nullptr)
            tmpNode = tmpNode->next;

        tmpNode = newNode;
    }

    
};

template <class T>
class Stack
{
private:
    Node *base;
public:

};