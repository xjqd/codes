#include <stdio.h>
int fibIterator(a, b, counter)
{
  if (counter==0) {
	return b;
  }
  printf("count=%d a=%d b=%d\n",counter, a, b);
  return fibIterator((a+b), a, counter-1);
}
int main()
{
 int m,i;
/*
 for(i=0; i< 10; i++)
 {
   m = fibIterator(5,8, i);
   printf("m=%d\n",m);
 }
*/
m = fibIterator(5,8, 6);
printf("m=%d\n",m);
return 0;
}
