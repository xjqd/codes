package main

import "fmt"

type Rect struct {
	x, y          int
	width, height int
}

func (r *Rect) Area() int {
	return r.width * r.height
}

func main() {
	rect1 := new(Rect)
	fmt.Println(rect1)
	fmt.Println(rect1.Area())
	rect2 := Rect{}
	fmt.Println(rect2)
	fmt.Println(rect2.Area())
	rect3 := &Rect{0, 0, 100, 200}
	fmt.Println(rect3)
	fmt.Println(rect3.Area())
	rect4 := Rect{x: 10, height: 20, width: 30}
	fmt.Println(rect4)
	fmt.Println(rect4.Area())
}
