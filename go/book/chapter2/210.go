package main

import "fmt"

func modify(arr [5]int) {
	arr[0] = 100
	fmt.Println(arr)
}
func main() {
	var arr3 [5]int = [5]int{11, 12, 1, 3, 14}
	var arr2 = [5]int{6, 7, 8, 9, 10}
	arr1 := [5]int{1, 2, 3, 4, 5}
	fmt.Println(arr3)
	fmt.Println("modify")
	modify(arr3)
	fmt.Println("after modify")
	fmt.Println(arr3)
	fmt.Println("end")
	fmt.Println(arr2)
	fmt.Println(arr1)
}
