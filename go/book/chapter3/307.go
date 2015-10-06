package main

import "errors"
import "fmt"

type File struct {
	n int
}

func (f *File) Read(buf []byte) (n int) {
	return 10
}
func (f *File) Write(buf []byte) int {
	return 11
}
func (f *File) Seek(off int64, whence int) (pos int64) {
	return 13.000
}
func (f *File) Close() {

}

type IFile interface {
	Read(buf []byte) (n int)
	Write(buf []byte) (n int)
	Seek(off int64, whence int) int64
	Close()
}

type IRead interface {
	/*
	   cannot use new(File) (type *File) as type IRead in assignment:
	      *File does not implement IRead (wrong type for Read method)
	      have Read([]byte) int
	      want Read([]byte) (int, error)

	*/
	//Read([]byte) (int, error)
	Read([]byte) int
}
type IWrite interface {
	Write(buf []byte) (n int)
}

func main() {
	var file1 IFile = new(File)
	var file2 IRead = new(File)
	var file3 IWrite = new(File)
	//var file4 ISeek = new(File)
	var err = errors.New("EOF")
	fmt.Println(file1, err)
	fmt.Println(file2, err)
	fmt.Println(file3, err)
}
