package main

import "fmt"
import "math/rand"

func Get_random_val(ch chan int) {
	for {
		val := rand.Intn(1000)
		ch <- val
	}
}

/*
func main() {
	ch := make(chan int, 1)
	go Get_random_val(ch)
	fmt.Println("random value=", <-ch)
}
*/
func TransferVal(ch chan int) chan int {
	go Get_random_val(ch)
	return ch
}

func main() {
	ch := make(chan int, 1)
	fmt.Println("ch=", ch)
	val := TransferVal(ch)
	fmt.Println("ch=", ch, "val=", val)
	fmt.Println("random value=", <-val)
	fmt.Println("random value=", <-val)
	ch = TransferVal(ch)
	fmt.Println("ch=", ch)
	fmt.Println("random value=", <-ch)
	fmt.Println("random value=", <-ch)
}
