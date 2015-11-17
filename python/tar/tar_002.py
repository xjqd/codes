#!/bin/python
import os
import tarfile

def py_files(members):
    for member in members:
        if os.path.splitext(member.name)[1] == ".go":
            yield member

tar = tarfile.open("gocode.tar.gz")
tar.extractall(members=py_files(tar))
tar.close()
