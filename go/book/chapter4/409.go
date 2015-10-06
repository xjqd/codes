package main

import "time"
import "fmt"

func main() {

	timeout := make(chan bool, 1)
	ch := make(chan int, 1)
	//ch <- 2
	/*go routine doesn't run it directly */
	go func() {
		fmt.Println(" in go func")
		time.Sleep(1e9)
		timeout <- true
	}()
	fmt.Println(" before select in main")
	select {
	case <-ch:
	case <-timeout:
	}
}
