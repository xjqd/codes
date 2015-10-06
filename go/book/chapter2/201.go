package main

import "fmt"

func main() {
	var v1 bool = true
	var v2 bool
	v2 = false
	v3 := (1 == 2)
	v4 := 1 << 4
	fmt.Print("v1=%d v2=%d v3=%d v4=%d\n", v1, v2, v3, v4)
	fmt.Print(v1, v2, v3, v4)
}
