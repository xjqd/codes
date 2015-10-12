#include <sys/types.h>
#include <stdio.h>

int main()
{
   pid_t result;
   int i=9;
   result = fork();
   if(result == -1)
   {
      printf("Fork error\n");
   }
   else if ( result == 0)
   {
      printf("child process is running...\n");
      /*
      sleep(1);
      */
      printf("The return value=%d in the child process(PID=%d)\n",result,getpid());
      while(i<10)
      {
        printf("child \t");
        i++;
      }
   }
   else 
   {
     printf("the return value=%d in the farther process(PID=%d)\n", result, getpid());
     while(i<10)
      {
        printf("farther \t");
        i++;
      }
   }
   return 0;
}
