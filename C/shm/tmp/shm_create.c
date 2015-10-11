#include <stdio.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include "global.h"

int main()
{
    printf("page size=%d\n", getpagesize());
    int shmid, ret;
    shmid=shmget(shared_shm_id, 10*4096, 0666|IPC_CREAT );
    if ( shmid > 0 )
    {
        printf ("create a shared memory segment %d\n", shmid);
    }
    struct shmid_ds shmds;
    ret = shmctl(shmid, IPC_STAT, &shmds);
    if ( ret == 0 )
    {
      printf("Size of memory segment is %d\n",shmds.shm_segsz );
      printf("Numbers of attaches %d\n", (int)shmds.shm_nattch);
    }
    else
    {
       printf("shmctl() call failed\n");
    }
    /*
    ret = shmctl(shmid, IPC_RMID, 0);
    if ( ret == 0 )
    {
      printf("shared memory removed\n");
    }
    else
    {
     printf("shared memory removed failed\n");
    }
    */
    printf("========\n");
    while(1)
    {
        sleep(60);
        break;
    }
    return 0;
}
