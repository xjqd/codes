package main

import (
	"fmt"
	"math/rand"
)

func generator() chan int {
	out := make(chan int, 1)
	go func() {
		for {
			fmt.Println("running...")
			out <- rand.Intn(100)
		}
	}()
	return out
}

func digit() chan int {
	out := make(chan int, 1)
	//for {
	fmt.Println("digit running..")
	out <- rand.Intn(400)
	//}
	return out
}

func digit2() int {
	fmt.Println("digit running..")
	out := rand.Intn(400)
	return out
}

func main() {
	handler := generator()
	fmt.Println("handler=", <-handler)
	fmt.Println("handler=", <-handler)
	d := digit()
	fmt.Println("digit for d=", <-d)
}
