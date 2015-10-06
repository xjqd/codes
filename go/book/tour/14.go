package main

import "fmt"

const Pi = 3.14

func main() {
	const world string = "hello world"
	const sum = 1 << 10
	fmt.Println(Pi, world, sum)
}
