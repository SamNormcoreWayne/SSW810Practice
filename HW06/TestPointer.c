#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *i;
    int a = 1;
    int *b = (int *)malloc(sizeof(int));
    *b = 3;

    i = &a;
    *i = 3;
    printf("%d %x %d \n", *i, i, a);

    i = b;
    printf("%d %x\n", *i, i);
    *i = 4;
    printf("%d %d %x %x\n", *i, *b, i, b);

    free(b);
    printf("%x %d", i, *i);
    free(i);
}