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
	ch := make(chan int, 1)
	//var ch chan int
	fmt.Println("ch=", ch)
	go generator(ch, 2)
	fmt.Println("checking....")
	go generator(ch, 7)
	fmt.Println("receiving data")
	fmt.Println("sleeping..")
	time.Sleep(10 * time.Second)
	fmt.Println("ch =", <-ch)
	fmt.Println("get one value")
	fmt.Println("sleeping..")
	time.Sleep(10 * time.Second)
	fmt.Println("ch =", <-ch)
	fmt.Println("get another value")
	time.Sleep(10 * time.Second)
}
