package main

import "fmt"

func main() {

	var slice1 = make([]string, 5, 10)
	slice2 := make([]int, 5, 10)
	var arr = []int{7, 8, 9, 10}
	fmt.Println("arr=", arr)
	slice2 = append(slice2, 1, 2, 3, 4)
	slice2 = append(slice2, arr...)
	fmt.Println("slice1=", slice1)
	fmt.Println("slice2=", slice2)
	fmt.Println("Cap=", cap(slice2), "len=", len(slice2))

}
