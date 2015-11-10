package main

import (
	"fmt"
	"runtime"
	"time"
)

func check() {
	time.Sleep(5 * time.Second)
}
func main() {
	fmt.Println(runtime.NumCPU())
	//runtime.GOMAXPROCS(runtime.NumCPU())
	runtime.GOMAXPROCS(1)

	for i := 0; i < runtime.NumCPU(); i++ {
		fmt.Println("checking i=", i)
		check()
	}
}
