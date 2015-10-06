package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m = map[string]Vertex{
	"Bell Labs": Vertex{10.234, 11.456},
	"Google":    Vertex{37.42, 5.68},
	/*The last comma is needed */
}

func main() {
	fmt.Println(m)
}
