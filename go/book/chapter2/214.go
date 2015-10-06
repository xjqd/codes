package main

import "fmt"

func main() {

	var p = [6]int{1, 2, 3, 4, 5, 6}
	/*
		var q []int
		q = p[4:]
	*/
	/*
		var q = p[4:]
	*/
	q := p[4:]
	fmt.Println(q)
}
