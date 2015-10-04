#include <stdio.h>

int fib(int n)
{
    if(n<=1){
	return n;
    }
   return fib(n-1) + fib(n-2);
}

int main()
{
   int i,ret;
   for(i=0; i< 10; i++) 
   {
     ret=fib(i);
     printf("fib=%d\n",ret);
   }
   return 0;
}
