#include <stdio.h>
#include "global.h"
int main()
{
    int shmid, i;
    shmid = shmget(shared_shm_id,0, 0);
    block=( MY_BLOCK_T* )shmat( shmid,( const void* )0,0 );
    for(i=0; i<100; i++)
    {
        sleep(1);
        sb.sem_num=0;
        sb.sem_op= -1;
        sb.sem_flg=0;
        if (semop(block->semID,&sb, 1)!= -1)
        {
            block->string[block->counter++]=(char)i+30;
            sb.sem_num=0;
            sb.sem_op=1;
            sb.sem_flg=0;
             if (semop(block->semID,&sb, 1)!= -1)
             {
                 printf( "Failed to release the semaphore\n" );
             }
        }
        else
        {
            printf( "Failed to acquire the semaphore\n" );
        }
    }
    shmdt(( void*)block);
    return 0;
}
