package main

import (
	"checkerror"
	"checksum"
	"fmt"
	"net"
	"os"
	//"readfully"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: ", os.Args[0], " host")
		os.Exit(1)
	}
	host := os.Args[1]
	conn, err := net.Dial("ip4:icmp", host)
	checkerror.CheckError(err)
	fmt.Println("test 111")
	var msg [512]byte
	msg[0] = 8
	msg[1] = 0
	msg[2] = 0
	msg[3] = 0
	msg[4] = 0
	msg[5] = 13
	msg[6] = 0
	msg[7] = 37
	len := 8
	check := checksum.CheckSum(msg[0:len])
	msg[2] = byte(check >> 8)
	msg[3] = byte(check & 255)

	fmt.Println("test 222")

	_, err = conn.Write(msg[0:len])
	checkerror.CheckError(err)

	fmt.Println("test 333")

	_, err = conn.Read(msg[0:])
	checkerror.CheckError(err)

	fmt.Println("test 444")

	fmt.Println("Get Response")
	if msg[5] == 13 {
		fmt.Println("Identifier match")
	}
	if msg[7] == 37 {
		fmt.Println("Sequence match")
	}
	os.Exit(0)
}
