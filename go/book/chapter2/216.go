package main

import "fmt"

func main() {
	v1 := []int{1, 2, 3}
	v2 := v1[:2]
	fmt.Println("v1=", v1)
	fmt.Println("v2=", v2)
}
