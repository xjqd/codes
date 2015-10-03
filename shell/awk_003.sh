BEGIN { i=1}
{for (; i<$3; i++) {
        printf("%d\t%.2f\n", i, $1 * (1 + $2) ^ i)
    }
    printf(" run %d times\n", i)
    i=0
}
END { printf ("end\n") }
