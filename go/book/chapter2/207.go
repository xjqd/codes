package main

import "fmt"

func main() {
	var val1 complex64
	val1 = 10 + 30i
	val2 := complex(10, 30)
	var val3 complex64 = 10 + 30i
	fmt.Print(val1)
	fmt.Print(val2)
	fmt.Print(val3)
}
