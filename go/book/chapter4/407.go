package main

import "fmt"
import "runtime"

func Print(ch chan int) {
	ch <- 2
	fmt.Println("print in Print")
}
func Print2(ch chan int) {
	val := <-ch
	fmt.Println("Print2 for val", val)
}
func main() {
	var ch1 chan int
	var ch2 chan int
	ch1 = make(chan int)
	ch2 = make(chan int)
	/* does it block all the thread
	    fatal error: all goroutines are asleep - deadlock!
		ch1 <- 2
	*/
	//	go Print(ch1)
	go Print2(ch2)
	runtime.Gosched()
	select {
	case <-ch1:
		fmt.Println("get from ch1")
	case ch2 <- 1:
		fmt.Println("write to ch2")
	default:
		fmt.Println("default")
	}
}
