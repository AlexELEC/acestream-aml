#!/bin/sh

ACEDIR='/acestream.engine'

export ANDROID_DATA=/system
export ANDROID_ROOT=/system
export ANDROID_STORAGE=/media
export PYTHONHOME=$ACEDIR/python
export PYTHONPATH=$ACEDIR/python/lib/python2.7/lib-dynload:$ACEDIR/python/lib/python2.7.zip:$ACEDIR/python/lib/python2.7
export PATH=$PATH:/bin:/sbin:$ANDROID_ROOT/bin:$PYTHONHOME/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ACEDIR/python/lib:$ACEDIR/python/lib/python2.7/lib-dynload

cd $ACEDIR
$PYTHONHOME/bin/python
