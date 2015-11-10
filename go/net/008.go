package main

import (
	"fmt"
	"runtime"
	"time"
)

func check(ch chan int, i int) {
	time.Sleep(5 * time.Second)
	ch <- i
}
func main() {
	fmt.Println(runtime.NumCPU())
	//runtime.GOMAXPROCS(runtime.NumCPU())
	runtime.GOMAXPROCS(1)

	ch := make([]chan int, runtime.NumCPU())
	for i := 0; i < runtime.NumCPU(); i++ {
		ch[i] = make(chan int)
	}

	for i := 0; i < runtime.NumCPU(); i++ {
		go check(ch[i], i)
	}
	for _, ok := range ch {
		fmt.Println(<-ok)
	}
}
