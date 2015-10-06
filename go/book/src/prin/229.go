package main

import "fmt"

func myprintf(args ...interface{}) {
	for _, arg := range args {
		switch arg.(type) {
		case int:
			fmt.Println("int")
		case float32:
			fmt.Println("float32")
		case string:
			fmt.Println("string")
		default:
			fmt.Println("unknow type")
		}
	}
}
func main() {
	v0 := int(10)
	var v1 = 20
	var v2 = 1.345
	v3 := "i am man"
	var v4 = 40
	var v5 = float32(10.0)
	myprintf(v0, v1, v2, v3, v4, v5)
}
