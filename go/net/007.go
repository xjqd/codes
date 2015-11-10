package main

import "fmt"

type shared struct {
	reader chan int
	writer chan int
}

func shared_routine(v shared) {
	val := 100
	for {
		select {
		case val = <-v.writer:
		case v.reader <- val:
		}
	}
}

func main() {
	v := shared{make(chan int), make(chan int)}
	go shared_routine(v)
	fmt.Println(<-v.reader)
	v.writer <- 10
	fmt.Println(<-v.reader)
}
