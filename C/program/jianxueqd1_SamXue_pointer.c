#include <stdio.h>
#include <stdlib.h>
#define maxlen 32
/*********************************************************************
**  remove_start
**
** It remove the '*" located between any alphabeta.
** key logic:
**    re-write the contents of the input pointer and remove the '*' between
**    first and last alphbeta
** Example:
**   It makes the ****AB*C***D*** become ****ABCD***
**
** INPUTS:
**   The pointer point to the strings needed to process.
** OUTPUTS:
**   None
** NOTE:
**   Need to process the input pointer directly, since the caller need it.
*********************************************************************/
void remove_start(char *s)
{
    char *first_alphabeta = NULL;
    char *last_alphabeta = NULL;
    int not_found = 0;
    char *p = s;
    int i = 0;
    /*figure out the first alphabeta*/
    while(*p)
    {
        if ( (*p != '*') && !not_found )
        {
            not_found = 1;
            first_alphabeta = p;
        }
        p++;
    }
    /*figure out the last alphabeta*/
    p--;
    while( *p == '*')
    {
        p--;
    }
    last_alphabeta = p;
    p=s;
    /* if the pointer no reach first alphabeta, do nothing */
    while( p < first_alphabeta)
    {
        i++;
        p++;
        
    }
    /*
     remove the '*' and just copy the alphabeta the pointer 
     between first and last alpahbeta
    */
    while ( p < last_alphabeta)
    {
        if(*p != '*')
        {
            s[i++] = *p;
        }
        p++;
    }
    /* conjuncte the '*' after the last alphabeta */
    while(*p)
    {
        s[i++] = *p;
        p++;
    }
    s[i] = 0;
}

int main()
{
    int i = 0;
    /* list 8 test cases */
    char string[8][maxlen] = {
      "",
      " ",
      "abcdefghijklmnopqrst",
      "********************",
      "****abcdefghijklmnop",
      "abcde***************",
      "***abcdefg**********",
      "***ab**cd****efg****",
      };
    while(string[i] && i<sizeof(string)/sizeof(string[0])){
        remove_start(string[i]);
        printf("output=%s\n",string[i]);
        i++;
    }
    return 0;
}
