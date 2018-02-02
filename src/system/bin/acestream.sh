#!/system/bin/sh

export ANDROID_ROOT=/system
export ANDROID_DATA=/system
export ANDROID_STORAGE=/media
export PYTHONHOME=/acestream.engine/python
export PYTHONPATH=/acestream.engine/python/lib/python2.7/lib-dynload
export PATH=$PYTHONHOME/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/acestream.engine/python/lib:/acestream.engine/python/lib/python2.7/lib-dynload

mkdir -p /bin
mkdir -p /sbin

if [ ! -f /system/bin/complete.install ]; then
  /system/bin/busybox --install -s
  /system/bin/busybox touch /system/bin/complete.install
fi

cd /acestream.engine
/acestream.engine/python/bin/python
