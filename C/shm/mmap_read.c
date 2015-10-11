#include "global.h"
#include <stdio.h>
#include <fcntl.h>
#include <sys/mman.h>
int main()
{
    int fd, i;
    MY_BLOCK_T *b_map;
    fd = open("./test", O_CREAT|O_RDWR|O_TRUNC,00777);
    if (fd < 0)
    {
            printf("open file failed");
    }
    printf("fd=%d\n", fd);
    /*
     lseek(fd,sizeof(MY_BLOCK_T)*20-1,SEEK_SET)
    if((i=lseek(fd,sizeof(MY_BLOCK_T)*20-1, SEEK_CUR))==-1)
    {
        printf("seek failed\n");
    }
     if((i=lseek(fd,2, SEEK_SET))==-1)
     {
        printf("seek failed\n");
     }
    printf("seek return=%d\n",i);
    write(fd, "a", 1);
     */
    lseek(fd,sizeof(MY_BLOCK_T)*10,SEEK_SET); 
    write(fd, "a", 1);
    b_map = (MY_BLOCK_T *) mmap( NULL,sizeof(MY_BLOCK_T)*10,PROT_READ|PROT_WRITE,
                                   MAP_SHARED,fd,0 );
    for(i=0; i<10; i++)
    {
        printf("semid=%d\tcounter=%d\tstring=%s\n",b_map->semID,b_map->counter, b_map->string);
        b_map++;
    }
     munmap(b_map,sizeof(MY_BLOCK_T)*10);
    close(fd);

}
