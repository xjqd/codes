package main

import "fmt"

func main() {
	v1 := []string{"ab", "c", "mn", "xy", "xxx"}
	var v2 []string = []string{"yyy"}
	copy(v2, v1)
	v3 := []string{"tttt"}
	fmt.Println("v2=", v2)
	copy(v1, v3)
	fmt.Println("v1=", v1)
}
