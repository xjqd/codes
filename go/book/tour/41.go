package main

import "fmt"

func main() {
	pow := make([]int, 10)
	for i := range pow {
		fmt.Println(i)
		pow[i] = 1 << uint(i)
	}
	for i, value := range pow {
		fmt.Println("i=", i, " value=", value)
	}
}
