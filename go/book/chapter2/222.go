package main

import "fmt"

func main() {
	var sum int
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
	for {
		sum++
		fmt.Println(sum)
		if sum > 100 {
			break
		}
	}

}
