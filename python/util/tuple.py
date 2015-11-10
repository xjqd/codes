#!/bin/python
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

_levelNames = {
    CRITICAL : 'CRITICAL',
    ERROR : 'ERROR',
    WARNING : 'WARNING',
    INFO : 'INFO',
    DEBUG : 'DEBUG',
    NOTSET : 'NOTSET',
    'CRITICAL' : CRITICAL,
    'ERROR' : ERROR,
    'WARN' : WARNING,
    'WARNING' : WARNING,
    'INFO' : INFO,
    'DEBUG' : DEBUG,
    'NOTSET' : NOTSET,
}

def getLevelName(level=None):
    print ("Level %s" % level)
    return _levelNames.get(level, ("Level %s" % level))

if __name__ == "__main__":
    s = getLevelName(level="ERRORiabc")
    print s
