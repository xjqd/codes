package two

type Istream interface {
	Write(buf []byte) (n int)
	Read([]byte) int
}

type Saction interface {
	Write(buf []byte) int
}
