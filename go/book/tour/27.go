package main

import "fmt"

func main() {

	type Vertex struct {
		x, y int
	}

	p := &Vertex{2, 3}
	fmt.Println(p.x)
	q := &p
	//q.x = 10
	//fmt.Println(&p, q, q.x, p.x)
	fmt.Println(&p, q, p.x, *p, *q, **q)
}
