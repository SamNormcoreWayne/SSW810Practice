#include <stdio.h>
#include <stdlib.h>

typedef struct BiTNode{
    int data;
    struct BiTNode *left, *right;
}BTNode, *BiTree;

typedef struct stack
{
    int *base;
    int *top;
    int size;
}Stack, * sNode;

int InitStack(Stack *stack)
{
    stack->base = (int *)malloc(sizeof(int) * 50);
    if (!stack->base)
        return -1;

    stack->top = stack->base;
    stack->size = 50;

    return 1;
}

int GetTop(Stack stack, int *a)
{
    if (stack.top = stack.base)
        return -1;
    a = stack.top - 1;

}

int CreateTree(BiTree *Tree)
{
    int node;

    scanf("%d", &node);
    if (-1 == node)
        *Tree = NULL;
    else
    {
        (*Tree)->data = node;

        printf("Input Left. \n");
        CreateTree(&(*Tree)->left);
        printf("Input right. \n");
        CreateTree(&(*Tree)->right);
    }

    return 1;
}

int PreOrdTraverse(BiTree Tree)
{

}
