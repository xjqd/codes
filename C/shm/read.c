#include <stdio.h>
#include "global.h"

int main()
{
    int i;
    int shmid;
    shmid = shmget(shared_shm_id,0,0 );
    if (shmid == -1)
    {
        printf("shared memory not existed\n");
        return 0;
    }
     block=( MY_BLOCK_T* )shmat( shmid,( const void* )0,0 );
     for (i=0; i<10; i++)
     {
         printf("block=%p\n",block);
         printf("semID=%d\n",block->semID);
         printf("counter=%d\n",block->counter);
         printf("string=%s\n",block->string);
         block++;
     }
     shmdt( ( void*)block );
}
