package main

import "fmt"

type Vertex struct {
	x, y int
}

func main() {
	v := new(Vertex)
	v.x, v.y = 10, 11
	/*
	   	m := new(Vertex{20, 21})
	       Vertex literal is not a type
	*/
	var m *Vertex = new(Vertex)
	m = v
	fmt.Println(v)
	fmt.Println(m)
}
