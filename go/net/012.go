package main

import "fmt"

func add(ch chan int) {
	//for {
	ch <- 10
	//}
}
func main() {
	ch := make(chan int, 1)
	for {
		go add(ch)
		fmt.Println(<-ch)
	}
	for {
	}

}
