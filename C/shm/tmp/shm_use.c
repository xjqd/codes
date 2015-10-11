#include <stdio.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <string.h>
#include "global.h"

int main()
{
    int shmid, ret;
    void *mem;
    printf("page size=%d\n", getpagesize());
    shmid=shmget(shared_shm_id,0, 0);
    if ( shmid >= 0 )
    {
      mem=shmat(shmid, (const void *)0, 0);
      if ( (long int)mem != -1 )
      {
         printf("shared memory attachmed in our address space is %p\n", mem);
	 strcpy( (char *)mem, "this is a test");
         printf("out from mem %s\n", mem);
      }
      else
      {
         printf("shmat() failed\n");
      } 
    }
    else
    {
       printf("shmget() failed\n");
    }
    while (1)
    {
       sleep(60);
       break;
    }
}
