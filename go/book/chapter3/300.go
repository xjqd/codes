package main

import "fmt"

type Integer int

func (r Integer) Add(a Integer) (ret Integer) {
	//func ADD(a Integer, b Integer) (ret Integer) {
	return r + a
}

func (r *Integer) Sub(t Integer) {
	*r = *r - t
}

func main() {
	var b Integer = 3
	fmt.Println(b)
	var a = b.Add(4)
	a = a.Add(4)
	fmt.Println(a)
	b.Sub(2)
	fmt.Println(b)
}
