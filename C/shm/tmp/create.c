#include "global.h"
#include <stdio.h>
#include <stdlib.h>

int main()
{
  int shmid;
  shmid = shmget(shared_shm_id, sizeof(MY_BLOCK_T)*10,  IPC_CREAT|0666 );
  if (shmid >= 0)
  {
     printf("creating the shared memory successfully\n");
     printf("shmid = %d\n", shmid);
     /*create and initialize the semaphore */
     block=(MY_BLOCK_T *)shmat(shmid, ( const void* )0,0);
     printf("block=%p\n", block);
     block->semID=semget(sem_id,1,IPC_CREAT|0666 );
     sb.sem_num=0;
     sb.sem_op=1;
     sb.sem_flg=0;
     semop(block->semID,&sb,1 );
     printf("create the semaphore success\n");
  }
  else
  {
    printf("creat shared memory failed\n");
  }
  return 0;
}
