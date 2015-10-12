#include <stdio.h>
#include <sys/sem.h>
#include "global.h"

int init_sem(int sem_id, int init_value)
{
   union semun sem_union;
   sem_union.val = init_value;
   if(semctl(sem_id, 0, SETVAL, sem_union)==-1)
   {
     printf("initialize semaphore failed\n");
     return -1;
   }
  return 0;
}

int del_sem(int sem_id)
{
  union semun sem_union;
  if(semctl(sem_id, 0, IPC_RMID, sem_union)==-1)
  {
     printf("delete semaphore failed\n");
     return -1;
  }
  return 0;
}

int sem_p(int sem_id)
{
  struct sembuf sem_union;
  sem_union.sem_num = 0;
  sem_union.sem_op = -1;
  sem_union.sem_flg = SEM_UNDO;
  if(semop(sem_id, &sem_union, 1)==-1)
  {
    printf("P operation failed\n");
    return -1;
  }
  return 0;
}

int sem_v(int sem_id)
{
  struct sembuf sem_b;
  sem_b.sem_num = 0;
  sem_b.sem_op = 1;
  sem_b.sem_flg = SEM_UNDO;
  if( semop(sem_id, &sem_b, 1) == -1)
  {
    printf("V operation failed\n");
    return -1;
  }
  return 0;
}
