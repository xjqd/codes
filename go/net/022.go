package main

import "fmt"

type Digit struct {
	x, y int
}

func Alloc_data() Digit {
	d := Digit{10, 20}
	return d
}

func main() {
	/*
		type Digit struct {
			x, y int
		}
	*/
	d := Alloc_data()
	fmt.Println("d=", d)
}
