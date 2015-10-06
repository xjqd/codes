package main

import "fmt"

func func3(x []int) {
	fmt.Println(x)
}

//func myfunc(x int, args []int) {
//func myfunc(x int, args ...int) {
func myfunc(x int, args ...interface{}) {
	for _, arg := range args {
		fmt.Println(arg)
	}
	fmt.Println("abc", args[:])
	fmt.Println(args[1:2])
	fmt.Println(args...)
	/*
		    invalid use of ... in call to func3
			func3(args...)
	*/

	//func3(args[1:2])
}

func main() {
	myfunc(1, 2, 3)
	myfunc(1, 2, 3, 4)
	myfunc(1, 2, 3, 4, 5)
}
