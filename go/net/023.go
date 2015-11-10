package main

func Out(ch chan int) {
	//for i := 0; i < 50; i++ {
	for {
		<-ch
	}
}
func main() {
	ch := make(chan int, 1)
	//for i := 0; i < 5000; i++ {
	for {
		go Out(ch)
		ch <- 1
	}
}
