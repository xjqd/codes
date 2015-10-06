package main

import "fmt"

func main() {
	/*
		        import "errors"
				f := func(x, y int) (ret int, err errors) { return x + y, err }
				a, ok := f(3, 4)
	*/
	f := func(x, y int) (ret int) { return x + y }
	a := f(3, 4)
	fmt.Println(a)
	fmt.Println(func(x, y int) (ret int) { return y - x }(4, 7))
}
