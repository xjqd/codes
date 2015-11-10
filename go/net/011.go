package main

import "fmt"

func generator(strings chan string) {
	strings <- "hi"
	strings <- "world"
	strings <- "good"
	strings <- "bye"
	close(strings)
}
func main() {
	strings := make(chan string)
	go generator(strings)
	for s := range strings {
		fmt.Println("%s\n", s)
	}
}
