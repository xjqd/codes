package main

import "fmt"

func main() {
	//var ch chan int = make(chan int, 1)
	ch := make(chan int, 1)
	for {
		select {
		case ch <- 0:
		case ch <- 1:
		}
		i := <-ch
		fmt.Println("Valued received:", i)
	}
}
