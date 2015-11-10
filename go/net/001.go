package main

import "fmt"
import "math/rand"

func digit(ch chan int) {
	ch <- rand.Intn(1000)
}

func main() {
	ch := make(chan int, 1)
	/*
			for i := 1; i < 10; i++ {
				go digit(ch)
				fmt.Println("digit=", <-ch)
			}
		for {
			go digit(ch)
			m := <-ch
			fmt.Println("digit=", m)
			if m == 2009 {
				break
			}
		}
	*/
	go digit(ch)
	m := <-ch
	fmt.Println("digit=", m)

}
