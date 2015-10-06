package main

import "fmt"

func checkif(x int) int {
	if a := 0; x == 0 {
		fmt.Println(a)
		return 5
	} else if x > 0 {
		fmt.Println("x!=0")
	}
	return x
}

func main() {
	a := checkif(0)
	fmt.Println(a)
}
