#include <stdio.h>
#include "global.h"
int checkFlg()
{
   if ( k == 1 )
      return 1;
}
int main()
{
  if (checkFlg())
  {
     k=0;
     sleep(1);
     k=1;
  }
  return 0;
}
