#include <stdio.h>
#include <sys/types.h>
#include <sys/sem.h>
int sem_id;
int main()
{
  pid_t ret;
  sem_id = semget(ftok(".",'a'),1,IPC_CREAT|0666);
  init_sem(sem_id,0);
  ret = fork();
  if(ret == -1 )
  {
     printf("fork error\n");
  }
  else if( ret == 0 )
  {
    sleep(2);
    /*sem_p(sem_id); 由于是0，如果一开始也P,会倒是系统死锁 */
    printf("child progress\n");
    printf("child process id=%d\n", getpid());
    sem_v(sem_id);
  }
  else
  {
    sem_p(sem_id);
    printf("farther process pid=%d ppid=%d\n",getpid(),getpid());
    sem_v(sem_id);
    del_sem(sem_id);
  }
  return 0;
}
