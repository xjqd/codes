#include <stdio.h>
#include "global.h"
int main()
{
  if (k==1)
  {
    while(k!=0)
    {
      if (k==0)
      {
	 break;
      }
    }
  }
  else if ( k == 0 )
  {
    k = 1;
    sleep(1);
    k = 0;
  }
  return 0;
}

