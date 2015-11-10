package main

import "fmt"

func main() {
	type Digit struct {
		x int
		y int
	}
	d := Digit{10, 20}
	fmt.Println("d=", d)
	//d1 := new(Digit(10, 20))
	d1 := new(Digit)
	d1.x = 100
	d1.y = 200
	fmt.Println("d1=", d1)
	d2 := Digit{1000, 2000}
	fmt.Println("d2=", d2)
	d3 := Digit{x: 1000, y: 25000}
	fmt.Println("d3=", d3)

}
