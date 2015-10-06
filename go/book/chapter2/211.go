package main

import "fmt"

func main() {

	v1 := [3]string{"abc", "efg", "hi"}
	var v2 = [2]rune{'c', 'h'}
	/* cannot use 1 (type int) as type [2]int in array element
	var v3 [2][2]int = [][2]int{1, 2, 3, 4}
	*/
	var v3 [2][2]int = [2][2]int{{1, 2}, {3, 4}}
	var v4 [2][2]int
	v4 = [2][2]int{{1, 2}, {3, 4}}
	fmt.Println(v1)
	fmt.Println(v2)
	fmt.Println(v3)
	fmt.Println(v4)
	for i, v := range v4 {
		fmt.Println("ele[", i, "]=", v)
	}
	fmt.Println("len(v4)=", len(v4))
}
