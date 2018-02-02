#!/bin/sh

export ANDROID_ROOT=/system
export ANDROID_DATA=/system
export ANDROID_STORAGE=/media
export PYTHONHOME=/acestream.engine/python
export PYTHONPATH=/acestream.engine/python/lib/python2.7/lib-dynload
export PATH=$PYTHONHOME/bin:$ANDROID_DATA/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/acestream.engine/python/lib:/acestream.engine/python/lib/python2.7/lib-dynload

cd /acestream.engine
/acestream.engine/python/bin/python
