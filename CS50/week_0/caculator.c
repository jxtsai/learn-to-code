#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("x:  ");
    int y = get_int("y:  ");
    if (x > y)
    {
        printf("X is greater than Y\n");
    }
    else
    {
        printf(" X is less than Y\n");
    }
    printf("The answer is %i\n", x + y);
}