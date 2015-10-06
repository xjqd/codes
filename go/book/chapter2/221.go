package main

import "fmt"

func main() {

	num := 12

	switch {
	case 0 < num && num < 3:
		fmt.Println("num 0 ~ 3")
	case 3 <= num && num < 6:
		fmt.Println("num 3 ~ 6")
	case 6 <= num && num < 10:
		fmt.Println("num 6 - 10")
	default:
		fmt.Println("default")
	}
}
