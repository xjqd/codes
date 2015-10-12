int k;
int sem_id;
union semun
{
   int val;
   struct semid_ds *buf;
   unsigned short *array;
};
/*
此定义已经在sys/sem.h 中
struct sembuf {
                ushort  sem_num;        在数组中信号量的索引值 
                short   sem_op;         信号量操作值(正数、负数或0)
                short   sem_flg;        操作标志，为IPC_NOWAIT或SEM_UNDO
        };
*/
