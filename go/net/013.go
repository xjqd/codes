package main

import "fmt"

func add(ch chan int) {
	for {
		ch <- 10
	}
}
func main() {
	ch := make(chan int, 1)
	for i := 0; i < 10; i++ {
		go add(ch)
		fmt.Println(<-ch)
	}

}
