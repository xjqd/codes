package main

import (
	"fmt"
	"time"
)

func produce(ch chan int, buf *[10]int) {
	fmt.Println("Starting Produce...")
	for i := 0; i < 10; i++ {
		buf[i] = i
		/*try yourself without following line*/
		ch <- i
		fmt.Println("Produce: buf[", i, "]=", i)
		time.Sleep(2 * time.Second)
	}
}
func consume(ch chan int, buf *[10]int) {
	fmt.Println("Starting Consume...")
	for i := 0; i < 10; i++ {
		fmt.Printf("Consume buf[%d]=%d\n", i, <-ch)
		/*try yourself with following line
		fmt.Printf("Consume buf[%d]=%d\n", i)
		*/
		time.Sleep(1 * time.Second)
	}
}
func main() {
	buf := [10]int{}
	//ch := make(chan int, 1)
	ch := make(chan int, 0)
	go produce(ch, &buf)
	go consume(ch, &buf)
	time.Sleep(50 * time.Second)
}
