package main

import "fmt"

func split(x, y int) (m, n int) {
	m = x + y
	n = x / y
	return
}

func main() {
	fmt.Println(split(20, 10))
}
