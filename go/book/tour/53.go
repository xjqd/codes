package main

import (
	"fmt"
	//"math"
)

type Vertex struct {
	X, Y int
}

func (v Vertex) Scale(f int) {
	v.X = v.X * f
	v.Y = v.Y * f
}

type Abser interface {
	Scale(f int)
}

func main() {
	x := Vertex{3, 4}
	x.Scale(5)
	fmt.Println(x)
	y := &Vertex{8, 10}
	y.Scale(6)
	fmt.Println(y)

	var a Abser = x
	var b Abser = y
}
