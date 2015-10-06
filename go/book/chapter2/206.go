package main

import "fmt"
import "math"

func IsEqual(f1, f2, p float32) bool {
	return math.Fdim(f1, f2) < p
}

func main() {

	/*
		var f1 float32
		var f2 float32
	*/
	/*
	   var f1, f2 float32
	*/
	var (
		f1 float32
		f2 string
	)

	f1 = 13.6789
	f2 = 13.7899
	m := IsEqual(f1, f2, 0.01)
	fmt.Print(m)
}
