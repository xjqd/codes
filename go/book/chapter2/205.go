package main

import "fmt"

func main() {
	var f1 float32
	f1 = 12
	f2 := 12.0
	var f3 float64 = 12.0

	//if float64(f1) == f2 {
	if (f1) == float32(f2) {
		fmt.Print("f1==f2\n")
	}
	if f2 == f3 {
		fmt.Print("f3==f2\n")
	}
}
