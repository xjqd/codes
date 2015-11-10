package main

import "fmt"

type test interface {
	check() bool
	add(x, y int) int
}

type Digit struct {
	x_pos int
	y_pos int
}

func (d Digit) check() bool {
	if d.x_pos > 0 && d.y_pos > 0 {
		return true
	} else {
		return false
	}
}
func (d *Digit) add(x, y int) int {
	if d.x_pos > 0 && d.y_pos > 0 {
		return d.x_pos + d.y_pos
	} else {
		return 0
	}
}
func main() {
	d := &Digit{10, 20}
	fmt.Println("d.x=", d.x_pos, "d.y=", d.y_pos)
	var if1 test = d
	m := if1.add(1, 2)
	fmt.Println("m=", m)
	//fmt.Println("x=", if1.x_pos, "y=", if1.y_pos)
}
