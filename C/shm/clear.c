#include "global.h"
#include <stdio.h>

int main()
{
    int shmid, i, ret;
    shmid = shmget(shared_shm_id, 0, 0);
    if (shmid == -1)
    {
        printf("shared memory not found\n");
    }
    block=( MY_BLOCK_T* )shmat( shmid,( const void* )0,0 );
    /*remove semaphore*/
    if((ret=semctl( block->semID,0,IPC_RMID))!=0)
    {
        printf("remove the semaphore failed\n");
    }
    /*remove shared memory*/
    if(shmctl(shmid,IPC_RMID,0)!=0)
    {
        printf("remove shared memory failed\n");
    }
    return 0;
}
