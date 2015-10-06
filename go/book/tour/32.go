package main

import "fmt"

func main() {
	var z = []int{}
	fmt.Println(z, len(z), cap(z))
	var x = []int{1, 2, 3, 4}
	var y = [4]int{1, 2, 3, 4}
	fmt.Println(x, y)
	fmt.Println(&x, &y)
	/*&&x doesn't exist*/
}
