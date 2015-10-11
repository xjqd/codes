#include <sys/sem.h>
#include <sys/ipc.h>
#include <sys/sem.h>

#define shared_shm_id 77777
#define sem_id 88888
#define MAX_STRING 14

typedef struct
{
    int semID;
    int counter;
    char string[ MAX_STRING+1 ];
}MY_BLOCK_T;
MY_BLOCK_T * block;
struct sembuf sb;

