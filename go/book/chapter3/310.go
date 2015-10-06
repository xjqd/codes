package main

import "fmt"

type Integer int

func (a Integer) Less(b Integer) bool {
	return a < b
}

type Lesser interface {
	Less(b Integer) bool
}

func main() {
	var a Integer = 1
	var b Lesser = a
	var c Lesser = &a
	fmt.Println(a, b, c)
}
