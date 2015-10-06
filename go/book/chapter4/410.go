package main

func main() {
	var ch1 chan int
	var ch2 <-chan int
	ch1 = make(chan int, 1)
	ch2 = ch1
	var ch3 chan<- int = chan<- int(ch1)
	ch4 := chan<- int(ch1)
}
