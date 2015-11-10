package main

import "fmt"
import "time"

func Generator(ch chan<- int) {
	for i := 2; ; i++ {
		fmt.Println("i=", i)
		ch <- i
	}
}

func Filter(in <-chan int, out chan<- int, prime int) {
	for {
		i := <-in
		fmt.Println("in Filter i=", i, "prime=", prime)
		if i%prime != 0 {
			out <- i
		}
	}
}

func main() {
	time.Sleep(2 * time.Second)
	ch := make(chan int)
	go Generator(ch)
	for i := 0; i < 10; i++ {
		prime := <-ch
		fmt.Println("prime=", prime)
		ch1 := make(chan int)
		go Filter(ch, ch1, prime)
		ch = ch1
	}
}
