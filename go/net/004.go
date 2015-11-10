package main

import "fmt"
import "math/rand"
import "time"

func generator(ch chan int, j int) {
	for {
		fmt.Println("calling...", j)
		m := rand.Intn(100)
		fmt.Println("m=", m)
		ch <- m
	}
}
func main() {
	ch := make(chan int, 0)
	fmt.Println("ch=", ch)
	go generator(ch, 2)
	//go generator(ch, 7)
	time.Sleep(10 * time.Second)
}
