package main

import "fmt"

type query struct {
	sql    chan string
	result chan string
}

func exec(q query) {
	q.result <- "get " + <-q.sql
}
func main() {
	q := query{make(chan string, 1), make(chan string, 1)}
	go exec(q)
	q.sql <- "select * from tables"
	result := <-q.result
	fmt.Println("result=", result)
}
