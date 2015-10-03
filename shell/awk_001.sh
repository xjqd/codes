#!/bin/awk
BEGIN { n=0; pay=0 }
$2>2 {n=n+1; pay=pay+$2*$3}
END { if (n>0) printf("%d employess total pay is %d\n", n,pay)
      else 
        printf("no empolyess\n")
        #print("no empolyess\n")
    }
