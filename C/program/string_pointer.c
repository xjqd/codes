#include <stdio.h>
int main()
{
    char *s = "abcdefg";
    /* not to use following assigne, becuase the content is in static stack */
    s[1] = 'B';
    printf("s=%s\n",s);
    /*
    char str[10];
    str="abcdefg";
    */
    /* for above case, you need to write like */
    char str[10]="abcdef";
    str[1]='B';
    printf("str=%s\n",str);
    return 0;
}
