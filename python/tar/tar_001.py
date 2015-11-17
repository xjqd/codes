#!/bin/python
import tarfile
tar = tarfile.open("./gocode.tar.gz")
tar.extractall()
tar.close()
