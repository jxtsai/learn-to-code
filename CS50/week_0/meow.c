#include <stdio.h>

void meow(int n );
// prototype of moew function, in case we did not define its content but delcare it at first hand

int main(void)
{

    meow(4);

}

void meow(int n){

     for (int i = 0; i < n; i ++){
        printf("I am a cat. \n");
     }

}
// define our function with void meow(void)
