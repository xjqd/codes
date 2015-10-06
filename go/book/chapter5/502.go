package main

import (
	//"bytes"
	"checkerror"
	"fmt"
	"net"
	"os"
	"readfully"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: ", os.Args[0], " host:port")
		os.Exit(1)
	}
	service := os.Args[1]
	conn, err := net.Dial("tcp", service)
	checkerror.CheckError(err)

	_, err = conn.Write([]byte("HEAD / HTTP/1.0\r\n\r\n"))
	checkerror.CheckError(err)

	result, err := readfully.ReadFully(conn)
	checkerror.CheckError(err)

	fmt.Println(string(result))

	os.Exit(0)
}
