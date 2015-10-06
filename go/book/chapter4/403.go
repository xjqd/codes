package main

import (
	"fmt"
	"runtime"
	"sync"
)

var counter int = 0

func Count(lock *sync.Mutex) {
	lock.Lock()
	counter++
	fmt.Println(counter)
	lock.Unlock()
}

func main() {
	/*
		    missing argument to conversion to sync.Mutex: sync.Mutex()
			lock := &sync.Mutex()
	*/
	lock := &sync.Mutex{}
	for i := 0; i < 10; i++ {
		go Count(lock)
	}
	fmt.Println("starting...")
	for {
		/* case1
		fmt.Println("fetch condition...")
		*/
		lock.Lock()
		c := counter
		/* case2 run a long time and get the chance to quit
		   fmt.Println("fetch condition...")
		*/
		lock.Unlock()
		runtime.Gosched()
		if c >= 10 {
			break
		}
	}
	fmt.Println("wait....")
}
