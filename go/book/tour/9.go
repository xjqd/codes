package main

import "fmt"

func swap(x, y string) (string, string) {
	return y, x
}
func main() {
	x, y := "world", "hello"
	fmt.Println(swap(x, y))
}
