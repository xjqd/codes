package main

import "fmt"

func modify(arr [][3]int) {
	arr[0][0] = 10
}

/*
func change(v4 [2]string) {
cannot use v4 (type []string) as type [2]string in argument to change
*/
func change(v4 [2]string) {
	v4[0] = "new"
	v4[1] = "old"
}
func main() {
	v1 := [2][3]int{{1, 2, 3}, {4, 5, 6}}
	fmt.Println("v1=", v1)
	v2 := v1[:1]
	modify(v2)
	fmt.Println("v2=", v2)
	fmt.Println("v1=", v1)
	v3 := [6]string{"hello", "world", "ni", "hao", "out", "get"}
	v4 := v3[:2]
	fmt.Println("v3=", v3)
	fmt.Println("v4=", v4)
	v4[0] = "china"
	v4[1] = "america"
	fmt.Println("v3=", v3)
	change(v4)
	fmt.Println("v3=", v3)
}
