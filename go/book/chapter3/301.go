package main

import "fmt"

func main() {
	var a = [3]int{1, 2, 3}
	var b = a
	b[0] = 10
	fmt.Println(a)
	fmt.Println(b)
	// cannot use &a (type *[3]int) as type [3]int in assignment
	var c = &a
	c[0] = 100
	fmt.Println(c)
	fmt.Println(a)
}
