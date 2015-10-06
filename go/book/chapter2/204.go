package main

import "fmt"

func main() {
	var m int32
	var n int64
	m = 32
	n = 64
	if m == 32 && n == 64 {
		fmt.Print("m==32, n==64\n")
	}
	if m < n { //nvalid operation: m < n (mismatched types int32 and int64)
		fmt.Print("m<n\n")
	}
}
