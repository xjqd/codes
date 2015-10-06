package main

import "fmt"

type Integer int

func (a Integer) Add(b Integer) (ret Integer) {
	ret = a + b
	return ret
}
func (a Integer) Less(b Integer) bool {
	return a < b
}
func main() {
	type LessAdder interface {
		Less(b Integer) bool
		Add(b Integer) (ret Integer)
	}
	var a Integer = 1
	var b LessAdder = a
	fmt.Println(a, b)
}
