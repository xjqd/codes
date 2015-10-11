#include <stdio.h>
#include <string.h>
int main()
{
    char str[14];
    int i;
    for(i=0; i<12; i++)
    {
        str[i]=0;
    }
    printf("len=%d\n",strlen("hello world"));
    memcpy(str, "hello world",strlen("hello world"));
    printf("str=%s\tlen=%d\n",str,strlen(str));
    return 0;
}
