package one

import "fmt"

type ReadWrite interface {
	Read(buf []byte) int
	Write(buf []byte) int
}
