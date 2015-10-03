{line[NR] = $0 }
END { i = NR;
      for(; i> 0; i--) {
	printf("%s\n", line[i]);
	 for ( j=0; i< NF; j++)
         {
	    printf("%s\n",line[i][j])
         }
      }
}
