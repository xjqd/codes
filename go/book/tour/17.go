package main

import "fmt"

func main() {
	sum := 1
	for sum = 0; sum < 100; sum++ {
		sum += sum
	}
	fmt.Println("sum=", sum)
}
