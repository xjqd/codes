package one

type ReadWrite interface {
	Read(buf []byte) int
	Write(buf []byte) int
}

type Read interface {
	Read(buf []byte) int
}
