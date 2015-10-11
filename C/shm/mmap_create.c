#include "global.h"
#include <stdio.h>
#include <fcntl.h>
#include <sys/mman.h>
int main()
{
    int fd, i;
    MY_BLOCK_T *b_map;
    printf("block=%d\n",sizeof(MY_BLOCK_T));
    //fd = open("./test", O_CREAT|O_RDWR|O_TRUNC,00777);
    fd = open("./test", O_CREAT|O_RDWR,00777);
    if (fd < 0)
    {
        printf("open file failed");
    }
    printf("fd=%d\n", fd);
    /*
    write(fd, "hello", strlen("hello"));
    write(fd, "world", strlen("world"));
    write(fd,"abcdefgh", 8);
    lseek(fd,sizeof(MY_BLOCK_T)*2,SEEK_SET); 
    lseek(fd,32,SEEK_SET); 
    lseek(fd,sizeof(MY_BLOCK_T)*20-1,SEEK_SET); 
    */
    //lseek(fd,0,SEEK_END); 
    lseek(fd,sizeof(MY_BLOCK_T)*10,SEEK_SET); 
     write(fd, "a", 1);
    b_map = (MY_BLOCK_T *) mmap( NULL,sizeof(MY_BLOCK_T)*10,PROT_READ|PROT_WRITE,MAP_SHARED,fd,0);
    close(fd);
    for(i=0; i<10; i++)
    {
        /*
        b_map->semID=i;
        b_map->counter=i;
        memcpy(b_map->string,"world hello",strlen("world hello"));;
        */
        (*b_map).semID=i;
        (*b_map).counter=i;
        memcpy((*b_map).string,"world hello",strlen("world hello"));;
        printf("sem=%d\tcount=%d\tstr=%s\n",b_map->semID,b_map->counter,b_map->string);
        b_map++;
    }
    printf(" initialize over \n ");
    sleep(2);
    /*
    msync(b_map, sizeof(MY_BLOCK_T)*10, MS_SYNC);
    */
    munmap(b_map,sizeof(MY_BLOCK_T)*10);
    return 0;
}
