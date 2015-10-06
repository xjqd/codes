package main

import "fmt"

func main() {

	type Logger struct {
		Level int
	}
	type Y struct {
		*Logger
		Name string
		*log.Logger
	}

	y := new(Y)
	fmt.Println(y.Logger, y.log.Logger)

}
