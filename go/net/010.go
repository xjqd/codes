package main

import "fmt"
import "time"

func worker(start chan bool, index int) {
	<-start
	fmt.Println("this is worker ", index)
}

func main() {
	start := make(chan bool)
	for i := 1; i <= 100; i++ {
		go worker(start, i)
	}
	for i := 1; i <= 100; i++ {
		if i%2 == 0 {
			start <- true
		} else {
			start <- false
		}
	}
	//close(start)
	time.Sleep(10 * time.Second)
	fmt.Println("end main")
}
