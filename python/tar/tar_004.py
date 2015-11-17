#!/bin/python
import tarfile
def reset(tarinfo):
    return tarinfo

with tarfile.open("gocode.tar.gz", "w|gz") as tar:
    for name in ["tar_001.py", "tar_002.py"]:
        tar.add(name)
